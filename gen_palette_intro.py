#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Generate chapter-zh/palette-intro-zh.tex and chapter-en/palette-intro-en.tex from a single data table.

Each palette card has three blocks:
  1. \subsection*{色彩哲学}  + paragraph
  2. fullwidth tabularx with the six colours
  3. \subsection*{<varies>}  + bulleted notes (one bullet per colour, or a small set of
     structural-logic bullets, depending on the source narrative).

Layout: all 24 palettes are emitted sequentially, separated by \par\bigskip;
LaTeX is allowed to break pages naturally between cards, and tabularx keeps each
six-colour table atomic on one page.
"""

import re

# =============================== ADD-A-PALETTE INTERFACE ③ ===============================
# Data source for the "Palette Introduction" chapter.  To contribute a new palette,
# APPEND a new dict to the P list below following the exact shape of an existing entry:
#   P.append(dict(
#       num=<index>, name='Your Palette Name',
#       philo_zh='...', philo_en='...',
#       rows=[((R,G,B), 'zh-name', 'en-name', 'original-name', 'R, G, B', 'gloss-zh', 'gloss-en'), ...x6],
#       sub2_zh='...', sub2_en='...',
#       bullets=[('BulletKey', 'desc-zh', 'desc-en'), ...x6],
#   ))
# Six rows MUST run from LIGHTEST to DARKEST.  After editing this file run
#   python3 gen_palette_intro.py
# to regenerate chapter-zh/palette-intro-zh.tex / chapter-en/palette-intro-en.tex.  Also remember to
# add matching \or branch (interface ①) and \bookpaletteguideentry row (interface ②)
# in Thomas-Tufte-bilingual-book.sty.  See README "参与贡献：添加你自己的配色".
# =========================================================================================

P = []  # palette list

# ---------------------------------------------------------------------------
# palette 0 — OUC Default
P.append(dict(
    num=0, name='OUC Default',
    philo_zh='这是模板出厂时的底色。蓝是青年学者的颜色——从清晨第一页讲义、午后图书馆窗台,到深夜实验台的冷光,蓝构成学术工作的整个色温。六层由浅入深的蓝刻意维持理性的克制,模拟一本书从翻开到合上的全过程;它不是一组要被注视的色,而是一组让文字自身被看见的色。这是写作者与读者之间最不打扰的契约,也是中国海洋大学海德学院 LaTeX 模板希望被使用者长期相处的方式。',
    philo_en='This is the factory ground tone of the template. Blue is the colour of the young scholar---from the first lecture page at dawn, through the library window at noon, to the cold lab light at midnight, blue spans the entire colour temperature of academic life. Six tones run from lightest to deepest, deliberately restrained, mirroring the arc of opening a book and closing it again. The palette does not ask to be looked at; it asks to let the words themselves be seen. This is the quietest possible contract between writer and reader, and the way the OUC Haide LaTeX template hopes to be used for the long haul.',
    rows=[
        ((239,246,255), '纸海蓝', 'Paper Foam', 'Paper Foam', '239, 246, 255', '翻开扉页时纸面反射的最浅一抹蓝,几近白', 'The faintest blue a page reflects at the moment of opening, almost white'),
        ((219,234,254), '冰晶蓝', 'Desert Foam', 'Desert Foam', '219, 234, 254', '实验室冷光下纸张投出的浅影,清洁而无负担', 'A page in shadow under cold lab light, clean and weightless'),
        ((96,165,250), '天玻璃蓝', 'Sea Smoke', 'Sea Smoke', '96, 165, 250', '窗外的天,是学者抬头喘息时的呼吸色', 'The window sky, the breath a scholar takes between paragraphs'),
        ((37,99,235), '讲堂蓝', 'Crisp Sky', 'Crisp Sky', '37, 99, 235', '黑板上一笔粉笔勾出的强调,是论证之色', 'A chalk stroke on the board, the colour of argument'),
        ((30,58,138), '深思蓝', 'Twilight Blue', 'Twilight Blue', '30, 58, 138', '思考最深处的暗蓝,接近梦的边界', 'The deepest blue of contemplation, near the edge of dream'),
        ((30,41,59), '铅墨石', 'Midnight Hull', 'Midnight Hull', '30, 41, 59', '钢笔留在笔记本上的最后一行字', 'The final line a pen leaves in the notebook'),
    ],
    sub2_zh='阅读弧线的色彩映射', sub2_en='Colour Mapping of the Reading Arc',
    bullets=[
        ('Paper Foam',       '纸海蓝是「开卷」的呼吸口,几近于白,允许任何一种文字以最少的视觉负担进入读者的眼睛',          'Paper Foam is the breath of "opening the book"---near-white, allowing any text to enter the reader\'s eye with the smallest visual cost'),
        ('Frost Crystal',    '冰晶蓝承担背景的次轻调,在长时间阅读中替代纯白,降低疲劳而不引起注意',                          'Frost Crystal carries the second-lightest weight, replacing pure white over long reads to lower fatigue without drawing attention'),
        ('Sky Glass',        '天玻璃蓝是六色中唯一带有「自然」气息的中调,把书页从全然的人工色阵列里拉回一次窗外的视野',     'Sky Glass is the only mid-tone with a hint of nature, pulling the page out of pure artificial colour and back to a glance out the window'),
        ('Lecture Sapphire', '讲堂蓝承担论证的强调职责,是六色中唯一允许「响」的色——但响得克制,像粉笔在板上敲下重音',     'Lecture Sapphire bears the duty of emphasis, the only tone permitted to be "loud"---yet loud with discipline, like chalk landing a stress on the board'),
        ('Reverie Navy',     '深思蓝把思考压向最深处,适合做长引文、关键定理、章节扉页的暗调主色',                            'Reverie Navy presses thought to its deepest layer, suiting long quotations, pivotal theorems, and chapter openings'),
        ('Slate Ink',        '铅墨石几乎是黑,却保有蓝的内核,是正文文字与所有结构线条最终落笔的颜色——书在它的颜色里收束',  'Slate Ink is almost black yet keeps a blue heart---the colour every line of body text and every structural rule finally lands in; the book closes inside it'),
    ]
))

# palette 1 — Brunneophobia
P.append(dict(
    num=1, name='Brunneophobia',
    philo_zh='名字直译为「恐褐症」,却用整组褐色直面这种偏见。褐不是廉价、不是过时,而是被现代审美刻意冷落的暖。从沙土、橘黄、铁锈到深焦,六色一路下沉,如同走进一间堆满旧书的木质工作室,鼻腔里有皮革、烟草、湿木的气息。色彩的勇气不在于鲜艳,而在于敢做被回避的那一种;这组配色把所有被嫌弃的褐重新收编进一种成熟的体面。',
    philo_en='The name literally reads "fear of brown", yet the palette faces that prejudice with nothing but brown. Brown is neither cheap nor dated; it is the warmth that modern taste has deliberately pushed aside. Six tones descend from desert sand and smoky tangerine through rust to the deepest scorched earth, like walking into a wood-panelled studio of old books, the air thick with leather, tobacco, and damp timber. Courage in colour is not brilliance---it is daring to be the shade everyone avoids, and brown, returned to itself, becomes the very definition of grown-up dignity.',
    rows=[
        ((238,211,180), '沙浪米', 'Lighthouse', 'Lighthouse', '238, 211, 180', '沙漠日出的最浅暖白,是褐色系的「呼吸口」', "The faintest warm white of desert dawn, the palette\\'s breath"),
        ((213,148,79), '烟橘', 'Sand Lily', 'Sand Lily', '213, 148, 79', '烟雾掩映下的橘黄,温暖却不张扬', 'Tangerine seen through smoke, warm but never loud'),
        ((213,148,79), '蜂蜡金', 'Reef Coral', 'Reef Coral', '213, 148, 79', '同色重复——表明这组褐刻意收紧色相', 'The same hue repeated---a deliberate narrowing of chroma'),
        ((180,69,15), '铁锈赤', 'Tidal Mauve', 'Tidal Mauve', '180, 69, 15', '暴露在湿气中数十年的铁,带着血与土', 'Iron left in damp air for decades, the colour of blood and soil'),
        ((86,67,53), '旧皮褐', 'Inkwell', 'Inkwell', '86, 67, 53', '老沙发与皮装订书脊的颜色,有岁月气息', 'The shade of an old sofa and a leather-bound spine, dense with years'),
        ((42,23,14), '焦土黑', 'Deep Tide', 'Deep Tide', '42, 23, 14', '篝火熄灭后炭灰里残留的最深褐', 'The deepest brown left in the ash after the campfire dies'),
    ],
    sub2_zh='褐色家族的内部结构', sub2_en='The Internal Order of the Brown Family',
    bullets=[
        ('Desert Foam',     '沙浪米作为整组配色的最浅调,承担所有「呼吸」与「留白」的职责,是褐色系里唯一不发声的色',                  'Desert Foam, as the lightest tone, carries every duty of breathing and negative space---the only brown in the set that does not speak'),
        ('Smoke Tangerine', '烟橘负责中段的温度,把整组配色从严肃拉回日常,是这组色与读者之间最亲切的接触面',                          'Smoke Tangerine governs the warmth of the middle band, returning the palette from gravity to daily life---the friendliest interface with the reader'),
        ('Beeswax Honey',   '蜂蜡金与烟橘共用色相,是整组配色刻意为之的「收紧」——意在证明克制本身即是力量',                           'Beeswax Honey shares a hue with Smoke Tangerine---a deliberate clenching, an argument that restraint itself is force'),
        ('Rust Crimson',    '铁锈赤是这组色彩的「锋」——它把柔和的褐推向有侵略性的红,是唯一允许刺痛的色',                            'Rust Crimson is the edge of the palette---it pushes gentle browns into an aggressive red, the only tone permitted to wound'),
        ('Aged Leather',    '旧皮褐承担文献质感,是图书馆、档案、皮装订所共享的深调,把读物的物质感留在了色彩里',                    'Aged Leather supplies the texture of archives---the deep tone shared by libraries, dossiers, and leather bindings, locking the physicality of reading into colour'),
        ('Scorched Earth',  '焦土黑是结构的根,所有上层暖色都因为它的存在而得以稳稳站立——克服恐褐症的最终一步,是承认黑的褐属性',  'Scorched Earth is the root of structure; every warm tone above it stands because it does---the final step in overcoming the fear of brown is to admit that black, too, is brown'),
    ]
))

# palette 2 — Van Dyke
P.append(dict(
    num=2, name='Van Dyke',
    philo_zh='致敬十七世纪佛兰德画家 Anthony van Dyck——他的肖像画用「凡戴克褐」打底,以薄釉层层堆叠出贵族肌肤的透光感。这组配色从他的画布生长而来:粉调的肌肤、淡紫的丝绸、暗红的天鹅绒、深褐的背景,皆是巴洛克肖像的标准物质。六色之间没有戏剧冲突,只有褪色后的体面;它们组成的不是一幅画,而是一幅画被时间洗过之后,墙上仍然挂着的那种气场。',
    philo_en='In tribute to Anthony van Dyck, the seventeenth-century Flemish portraitist whose ground colour, Van Dyke Brown, layered glaze upon glaze to lend aristocratic skin its translucent glow. The palette grows out of his canvas itself: powdered flesh tones, lilac silk, crimson velvet, deep brown ground---all standard materials of Baroque portraiture. There is no drama between the six tones, only the composure left after fading; together they do not form a painting so much as the atmosphere a painting leaves on a wall once time has washed across it.',
    rows=[
        ((236,194,188), '肌肤粉', 'Carnation Skin', 'Vleeskleur', '236, 194, 188', '巴洛克肖像中贵族面颊的薄釉粉调', "The thin-glazed pink of an aristocrat\\'s cheek in Baroque portraiture"),
        ((169,159,191), '丝绸藤', 'Silken Wisteria', 'Zijden Sering', '169, 159, 191', '折光丝绸在阴影里的淡紫,优雅而冷', 'The lilac silk catches in shadow, elegant and cool'),
        ((169,159,191), '烟雾紫', 'Smoke Lilac', 'Rooklila', '169, 159, 191', '同前——丝绸两面在画布上几乎不分', 'As above---both sides of the silk are barely distinct on canvas'),
        ((191,113,133), '玫瑰呢', 'Rose Velvet', 'Rozenfluweel', '191, 113, 133', '天鹅绒礼服里渗出的玫瑰红,沉而不艳', 'The rose that bleeds through velvet, deep without being loud'),
        ((68,60,94), '暗紫绒', 'Plum Plush', 'Pruimenpurper', '68, 60, 94', '背景帷幕的深紫,把光衬得更亮', 'The deep plum of the backdrop drapery, throwing the highlights brighter'),
        ((61,43,39), '凡戴克褐', 'Van Dyke Brown', 'Van Dijck-bruin', '61, 43, 39', '该画家的标志底色,以沥青颜料调和而成', "Van Dyck\\'s signature ground, mixed from bitumen pigment"),
    ],
    sub2_zh='肖像深度的色彩映射', sub2_en='Colour Mapping of Portrait Depth',
    bullets=[
        ('Carnation Skin', '肌肤粉是画面最前景——画中人物的面颊、手指、颈侧,是观看者第一眼接触到的「人」',                'Carnation Skin sits at the front---the cheek, the hand, the neck of the figure, the first "person" the viewer meets'),
        ('Silken Wisteria','丝绸藤是衣料的高光,把柔软的折光感留在了色相中,优雅而带着距离',                                 'Silken Wisteria is the silk\'s highlight, holding softness of refraction in the hue---elegant with distance'),
        ('Smoke Lilac',    '烟雾紫与丝绸藤同色,刻意制造重复,呼应巴洛克绘画里对单色叠层的偏爱',                            'Smoke Lilac shares its hue with Silken Wisteria, a deliberate repetition that echoes Baroque painting\'s love of monochromatic layering'),
        ('Rose Velvet',    '玫瑰呢是中景礼服的颜色,把人物从画中抬起、推近,是这组配色的色温支点',                          'Rose Velvet is the mid-ground gown, lifting and pushing the figure forward---the colour-temperature pivot of the set'),
        ('Plum Plush',     '暗紫绒是背景帷幕,负责把前景的人物从黑暗中托出,自己几乎不被注意',                              'Plum Plush is the curtain behind, lifting the figure out of darkness while almost escaping notice itself'),
        ('Van Dyke Brown', '凡戴克褐是整幅画的「地」——是颜料、画布、画框、墙面共同沉淀下来的底色,任何高光都因它而立',  'Van Dyke Brown is the "ground" of the whole work---the colour deposited by pigment, canvas, frame, and wall together; every highlight stands only because it does'),
    ]
))

# palette 3 — Back in Black
P.append(dict(
    num=3, name='Back in Black',
    philo_zh='致敬 AC/DC 1980 年的同名专辑,但配色本身比摇滚更克制。粉与灰柔化了黑的攻击性,使整组色更接近后朋克美学:皮夹克、烟雾、舞台灯熄灭后那一刻的余温。粉是疤痕,黑是夜——它们之间所有的灰,是青春过后还留在身体里的回声。这是一组「成熟版的叛逆」,把锋芒收进了体面之内。',
    philo_en='In tribute to AC/DC\'s 1980 album, though the palette itself is more restrained than rock. Pink and grey soften the aggression of black, pushing the set towards a post-punk aesthetic: leather jacket, smoke, the residual warmth right after the stage lights die. Pink is the scar, black is the night---every grey between them is the echo youth leaves inside the body. This is a grown-up version of rebellion, with its edge folded inside a composed surface.',
    rows=[
        ((240,217,228), '婴儿粉', 'Powder Pink', 'Powder Pink', '240, 217, 228', '黑暗里唯一不设防的颜色,是叛逆的反面', 'The only undefended colour in the dark, the opposite of rebellion'),
        ((193,160,172), '灰玫瑰', 'Dust Rose', 'Dust Rose', '193, 160, 172', '蒙了一层烟的粉,失去鲜艳后的体面', 'Pink with a film of smoke, dignity after the brightness has gone'),
        ((193,160,172), '烬粉', 'Ember Pink', 'Ember Pink', '193, 160, 172', '重复以加强中调,粉的两种语义并置', 'Repeated to strengthen the mid-band; two semantics of pink, side by side'),
        ((128,108,121), '雾紫灰', 'Smoky Mauve', 'Smoky Mauve', '128, 108, 121', '舞台灯下烟雾的灰紫,既不明也不暗', 'The smoke-grey purple under stage light---neither bright nor dim'),
        ((74,63,75), '黑天鹅绒', 'Black Velvet', 'Black Velvet', '74, 63, 75', '皮夹克的暗影,介于黑与紫之间', 'The shadow of a leather jacket, between black and purple'),
        ((22,19,21), '夜墨', 'Inkwell Black', 'Inkwell Black', '22, 19, 21', '一组配色最沉的锚点,几乎黑', 'The deepest anchor of the set, all but pure black'),
    ],
    sub2_zh='后朋克美学的色彩映射', sub2_en='Colour Mapping of a Post-Punk Aesthetic',
    bullets=[
        ('Powder Pink',  '婴儿粉是这组配色的「不设防」——它是黑底之上唯一一个温柔的入口,叛逆的反面才是叛逆的内核',          'Powder Pink is the unguarded entry---the only soft door above the black ground; rebellion\'s tender opposite is rebellion\'s core'),
        ('Dust Rose',    '灰玫瑰把粉的鲜艳压了下去,是青春之后留下的余韵,优雅地承认了「不再年轻」',                          'Dust Rose presses the brightness out of pink---the after-tone of youth, elegantly admitting it is no longer young'),
        ('Ember Pink',   '烬粉与灰玫瑰共享色相,是「重复即强调」的视觉修辞,把中调的灰玫瑰提升为整组色的真正核心',          'Ember Pink shares its hue with Dust Rose---a repeat-as-emphasis figure that promotes the mid-band into the true centre of the palette'),
        ('Smoky Mauve',  '雾紫灰是舞台烟雾的颜色,过渡了粉与黑,使两端的对立看起来像同一种情绪的两面',                       'Smoky Mauve is the smoke under the lights, bridging pink and black so the two extremes look like two faces of one mood'),
        ('Black Velvet', '黑天鹅绒是皮夹克的暗影,带着紫的呼吸——黑不必是死的,它可以是一种被穿在身上的物质',                'Black Velvet is the shadow of a leather jacket, breathing with purple---black does not have to be dead; it can be a substance worn on the body'),
        ('Inkwell Black','夜墨是最沉的锚点,接近纯黑却保有微紫底调,是整组色的句号——但句号之后还可以有下一首歌',          'Inkwell Black is the deepest anchor, near pure black yet keeping a violet undertone---the period of the palette, though even after a period the next song still plays'),
    ]
))

# palette 4 — Belle of the Ball
P.append(dict(
    num=4, name='Belle of the Ball',
    philo_zh='舞会上那位最被注视的女子从不穿原色——她穿的是被无数烛光暖化过的旧色:陶土、铜锈、橄榄、绛红。这组配色拒绝二十世纪的合成染料,从十九世纪欧洲晚宴厅与殖民地热带气候的混合美学中提取——壁炉、桃花心木、暮色窗帘、染了酒渍的桌布。被注视并不靠鲜艳,而靠所有颜色都已被时间柔化过的那种「被生活过的高级感」。',
    philo_en='The most-watched woman at the ball never wears primaries---she wears the old tones that countless candle flames have warmed: terracotta, verdigris, olive, deep crimson. The palette refuses twentieth-century synthetic dyes and is drawn instead from the mixed aesthetic of the nineteenth-century European salon and its colonial tropics---fireplace, mahogany, evening curtain, wine-stained linen. Being looked at depends not on brilliance but on that "lived-through" elegance every tone wears once time has softened it.',
    rows=[
        ((226,203,192), '香槟珠光', 'Champagne Pearl', 'Champagne Pearl', '226, 203, 192', '舞会大厅烛光下女子肌肤的珠光底色', 'The pearled skin tone of a woman under candlelight in the ballroom'),
        ((206,171,150), '玫瑰陶土', 'Rose Terracotta', 'Rose Terracotta', '206, 171, 150', '复古口红与陶土色的中间调,被注视的暖色', 'A mid-tone between vintage lipstick and terracotta---the warmth of being watched'),
        ((210,135,106), '陶釉橘', 'Glazed Clay', 'Glazed Clay', '210, 135, 106', '陶器釉面的橘红,温润而成熟', 'The orange-red of glazed pottery---warm, mature, hand-thrown'),
        ((229,74,57), '辣椒朱', 'Chilli Scarlet', 'Chilli Scarlet', '229, 74, 57', '热带气候里晾在阳光下的辣椒色,是这组配色的「亮点」', 'The scarlet of chilli peppers drying in tropical sun---the bright accent of the set'),
        ((118,118,44), '橄榄绿', 'Olive Verdigris', 'Olive Verdigris', '118, 118, 44', '橄榄叶被氧化后的中性绿,带些铜锈', 'Olive leaves oxidised to a neutral green with a bronze edge'),
        ((53,77,4), '苔藓深绿', 'Moss Deepwood', 'Moss Deepwood', '53, 77, 4', '桃花心木家具与深色窗帘的森林暗调', 'The forest-dark tone of mahogany furniture and deep curtains'),
    ],
    sub2_zh='被注视者的色彩策略', sub2_en='Colour Strategy of the One Being Watched',
    bullets=[
        ('Champagne Pearl', '香槟珠光是被烛光暖化的肌肤底色,是整组配色的「呼吸」,也是被注视者最不设防的一层',           'Champagne Pearl is skin warmed by candlelight---the breath of the palette and the most undefended layer of the watched figure'),
        ('Rose Terracotta', '玫瑰陶土承担「复古性感」,是被时间筛过的口红色,既是装饰也是身份的证明',                       'Rose Terracotta carries vintage allure---a lipstick filtered through time, both ornament and proof of standing'),
        ('Glazed Clay',     '陶釉橘是手作之色,把工业感从配色中排除,留下手心温度与陶土的物质感',                            'Glazed Clay is the colour of handcraft, banishing industry from the palette and keeping in its place the warmth of a palm and the substance of earth'),
        ('Chilli Scarlet',  '辣椒朱是全组唯一允许「亮」的色,是裙摆的红、戒指的红、唇上最后一笔的红——但只能小面积出现',  'Chilli Scarlet is the only tone permitted to be bright---the red of a hem, a ring, a final lipstick touch---and only ever in small area'),
        ('Olive Verdigris', '橄榄绿是这组色彩的冷调支点,把所有热带暖色拉回欧洲晚宴厅的克制,是配色的色温调节器',         'Olive Verdigris is the cool pivot, pulling every tropical warm back into the restraint of a European salon---the palette\'s thermostat'),
        ('Moss Deepwood',   '苔藓深绿是背景与家具的暗调,是这组配色的「重」,没有它,所有的亮都会失去支点',                 'Moss Deepwood is the background and the furniture, the gravity of the set---without it, every bright tone would lose its pivot'),
    ]
))

# palette 5 — Pine Tree
P.append(dict(
    num=5, name='Pine Tree',
    philo_zh='以一棵北方松树作为坐标,从树冠到树根逐层收色:阳光打在新生针叶上的暖金、被风吹松动的旧针、午后树荫里的玫瑰陶土、树干裂痕里渗出的赭色,以及最底层埋在腐殖土里的森林暗墨。配色逻辑刻意离开「绿色」——一棵真正的松树在视觉上远比绿色复杂得多,它的颜色其实是阳光、岁月、土壤、伤口与影子共同写下的一段年表。',
    philo_en='Anchored on a single northern pine, the palette descends from canopy to root: warm gold where sun strikes the new needles, the loosened old needles tossed by wind, rose-clay shadow under the afternoon canopy, ochre seeping from cracks in the trunk, and the dark forest ink buried in the humus below. The set deliberately leaves "green" behind---a real pine, seen carefully, is far more complex than green; its colour is a chronology jointly written by sunlight, weather, soil, wounds, and shadow.',
    rows=[
        ((238,200,111), '阳针金', 'Sunlit Needle', 'Sunlit Needle', '238, 200, 111', '阳光打在新生针叶上的暖金', 'Warm gold where sunlight strikes the new needles'),
        ((222,166,32), '蜂蜜松脂', 'Honey Resin', 'Honey Resin', '222, 166, 32', '树皮裂口渗出的松脂金,是松树自愈的颜色', "Pine resin oozing from a crack in the bark, the tree\\'s self-healing gold"),
        ((222,166,32), '陈年金', 'Aged Gold', 'Aged Gold', '222, 166, 32', '同色再现,使中调金更稳', 'The same gold returned, steadying the mid-band'),
        ((177,120,133), '幽影玫瑰', 'Shadow Rose', 'Shadow Rose', '177, 120, 133', '午后树荫里的玫瑰陶土,带紫调', 'Rose-clay in the afternoon shade, with a violet edge'),
        ((167,88,26), '树皮赭', 'Bark Ochre', 'Bark Ochre', '167, 88, 26', '树干主体的赭褐,是松树最诚实的颜色', "The ochre brown of the trunk itself---the tree\\'s most honest colour"),
        ((43,47,34), '林墨', 'Forest Ink', 'Forest Ink', '43, 47, 34', '腐殖土与树根处的森林暗墨', 'The dark forest ink of humus and root'),
    ],
    sub2_zh='松树年表的色彩映射', sub2_en='Colour Mapping of a Pine Tree\'s Chronology',
    bullets=[
        ('Sunlit Needle',  '阳针金是松树的「今天」——新生的、被光选中的、还没有故事的那一段时间',                              'Sunlit Needle is the pine tree\'s "today"---the newly-grown, sunlight-chosen tip that has no story yet'),
        ('Honey Resin',    '蜂蜜松脂是松树的「伤口」——树脂封住裂痕,使损伤变成琥珀,是这组色彩最具时间感的一色',                'Honey Resin is the wound---resin sealing a crack into amber, the tone most charged with time in the entire palette'),
        ('Aged Gold',      '陈年金与蜂蜜松脂共享色相,是中调金的「再说一遍」,把时间在颜色里复读一次',                          'Aged Gold shares its hue with Honey Resin---a "say it again" of the mid-band gold, time recited once more in colour'),
        ('Shadow Rose',    '幽影玫瑰是松树投在地面的紫红色阴影,是树与土壤之间的呼吸界面',                                       'Shadow Rose is the violet shadow the pine casts on the ground---the breathing interface between tree and earth'),
        ('Bark Ochre',     '树皮赭是树干本体,是最不需要解释的色——它的赭褐就是松树这个生命体的物质本色',                         'Bark Ochre is the trunk itself, the colour needing no explanation---a pine\'s very substance, named'),
        ('Forest Ink',     '林墨是松树的「根之色」,沉在腐殖土里,接近黑而仍属绿——它告诉我们,一棵活树的根,从不真正与黑相同',  'Forest Ink is the root colour, sunk in humus, near black yet still green---reminding us that a living root is never quite the same as black'),
    ]
))

# palette 6 — Provence Blue
P.append(dict(
    num=6, name='Provence Blue',
    philo_zh='普罗旺斯的蓝从不属于海——它属于薰衣草田尽头那片被夕阳压低饱和的蓝灰,属于午后石灰岩房屋窗框上经年褪色的孔雀蓝,属于一户人家晾在院里的旧亚麻床单与铁锈门把手共同呼吸的色温。这组配色拒绝地中海明信片式的浪漫,选择更内陆、更乡村、更被时间柔化过的法国南部蓝调——它的浪漫不在颜色的鲜艳里,而在颜色被使用过后留下的痕迹里。',
    philo_en='Provençal blue does not belong to the sea---it belongs to the blue-grey beyond a lavender field that the setting sun has desaturated, to the peacock paint flaking from a limestone window-frame after years, to the warm air shared by old linen sheets drying in a courtyard and a rusted iron handle. The palette refuses the postcard-Mediterranean romance and chooses an inland, rural, time-softened southern-French blue---its romance lives not in the brightness of the colour but in the trace the colour leaves once it has been used.',
    rows=[
        ((170,188,175), '橄榄银灰', 'Olive Silver', "Argent d'Olivier", '170, 188, 175', '橄榄树叶背面的银灰,带绿调', 'The silver-grey underside of an olive leaf, with a green note'),
        ((137,156,154), '雾镜蓝', 'Mist Mirror', 'Miroir de Brume', '137, 156, 154', '清晨雾气压在水面上的灰蓝', 'Morning mist pressed onto water, a grey-blue'),
        ((137,156,154), '宿雨青', 'Spent Rain', "Pluie Pass\\'ee", '137, 156, 154', '同色再现,巩固中调', 'Repeated, steadying the middle band'),
        ((110,124,139), '石窗蓝', 'Window Stone Blue', 'Bleu de Volet', '110, 124, 139', '石灰岩房屋窗框上的孔雀蓝褪色后的色', 'The peacock blue of a limestone window-frame, faded'),
        ((82,92,121), '薰衣草夜', 'Lavender Dusk', "Cr\\'epuscule Lavande", '82, 92, 121', '薰衣草田尽头被夕阳压低的暗紫蓝', 'The deep violet-blue at the far edge of a lavender field under sunset'),
        ((53,66,94), '橄榄夜空', 'Olive Night', "Nuit d'Olivier", '53, 66, 94', '橄榄园上方夜空的深蓝,带土壤气息', 'The deep blue night sky above the olive grove, with the smell of earth'),
    ],
    sub2_zh='南法乡村蓝调的色彩结构', sub2_en='Colour Structure of Rural Southern-French Blue',
    bullets=[
        ('Olive Silver',      '橄榄银灰是这组色彩里唯一的绿,是橄榄树叶背面在风里翻起的银光,是普罗旺斯空气的物质化',     'Olive Silver is the only green in the palette---the silver flash of an olive leaf turning in the wind, Provençal air made matter'),
        ('Mist Mirror',       '雾镜蓝是清晨水面的镜像,把蓝从天空借回地面,呼吸感最强的中调',                                'Mist Mirror is the dawn reflection on water, lending blue from the sky to the ground---the most breathable mid-tone'),
        ('Spent Rain',        '宿雨青与雾镜蓝同色,是「雨后第二日」的色温,刻意重复以加强配色的湿度',                          'Spent Rain shares its hue with Mist Mirror, the colour temperature of the second day after a rain---repeated to deepen the humidity of the palette'),
        ('Window Stone Blue', '石窗蓝把这组色彩从自然带回人造——它是被无数次刷过、又被无数次淡去的人手痕迹',                'Window Stone Blue pulls the palette out of nature back into the made---a hand-trace painted many times and faded many times more'),
        ('Lavender Dusk',     '薰衣草夜是配色的灵魂——它把薰衣草从「紫」推向「暗紫蓝」,这一步,正是普罗旺斯之所以为普罗旺斯', 'Lavender Dusk is the soul of the set---it pushes lavender from "violet" into "deep violet-blue", and that single step is exactly what makes Provence Provence'),
        ('Olive Night',       '橄榄夜空是这组色彩的根,把白日的所有蓝色收进了一片夜空,接近黑而仍是蓝',                       'Olive Night is the root, gathering every daytime blue back into a single sky, near black yet still blue'),
    ]
))

# palette 7 — Fresco Blue
P.append(dict(
    num=7, name='Fresco Blue',
    philo_zh='来自意大利文艺复兴时期教堂壁画的天空——那种被湿壁画(Fresco)技法吸入灰泥里、再被五百年烛烟氧化过的青蓝。它不是天空真实的颜色,而是匠人用青金石、孔雀石与石灰浆调出的「神圣的天空」,介于人间与天国之间。这组配色从最浅的天到最深的夜按梯度排列,模拟壁画从穹顶向地面跌落时蓝色的层层加深——它是一种被建筑收容过的天。',
    philo_en='From the church-fresco skies of the Italian Renaissance---the azure that fresco technique drew into the lime plaster and that five centuries of candle smoke have since oxidised. It is not the real colour of sky but the "sacred sky" mixed by craftsmen out of lapis lazuli, malachite, and lime: a blue between earth and heaven. The palette steps from the palest sky to the deepest night, mimicking the way fresco blue deepens as the wall falls from dome to floor---a sky housed inside architecture.',
    rows=[
        ((166,224,244), '穹顶浅天', 'Vault Sky', 'Cielo di Volta', '166, 224, 244', '教堂穹顶最高处壁画的浅蓝', 'The palest blue at the highest point of a vaulted fresco'),
        ((71,169,207), '钴釉蓝', 'Cobalt Glaze', 'Vetrina Cobalto', '71, 169, 207', '青金石与石灰浆调和后的中调蓝', 'The mid-blue mixed from lapis lazuli and lime wash'),
        ((71,169,207), '青金蓝', 'Lapis Renewed', 'Lapislazzuli', '71, 169, 207', '同色再现,巩固壁画的中段', 'Repeated, steadying the mid-band of the fresco wall'),
        ((9,121,158), '深殿蓝', 'Apse Blue', "Azzurro d'Abside", '9, 121, 158', '教堂半圆殿背景里五百年未褪的深蓝', 'The deep blue still unfaded after five centuries in the apse'),
        ((4,75,102), '夜祷蓝', 'Vigil Blue', 'Azzurro della Veglia', '4, 75, 102', '夜祷时灯火映在壁画下半部分的暗蓝', 'The dark blue cast onto the lower fresco during night vigil'),
        ((2,31,46), '地宫蓝', 'Crypt Blue', 'Azzurro della Cripta', '2, 31, 46', '地宫与暗廊里壁画几近隐没的最深蓝', 'The deepest blue, almost vanished, in crypt and shadowed gallery'),
    ],
    sub2_zh='壁画天空的垂直色谱', sub2_en='The Vertical Spectrum of a Fresco Sky',
    bullets=[
        ('Vault Sky',     '穹顶浅天是壁画最高处,光线打在灰泥上反射回来的浅蓝,是这组配色的「天」',                          'Vault Sky is the highest point of the fresco, the pale blue light bounces off the plaster---the "heaven" of the palette'),
        ('Cobalt Glaze',  '钴釉蓝是中段的主调,是教堂内信众抬头时看见的那一抹饱满',                                            'Cobalt Glaze is the dominant mid-tone, the full blue a worshipper sees when they look up inside the church'),
        ('Lapis Renewed', '青金蓝与钴釉蓝同色,是「再次确认」——壁画的蓝从不依靠一次涂抹,它依靠层层叠加',                     'Lapis Renewed shares its hue with Cobalt Glaze, the "reaffirmation"---fresco blue never relies on one stroke; it relies on layering upon layering'),
        ('Apse Blue',     '深殿蓝是教堂建筑里光线最难抵达的深处,壁画在那里凝固成不褪色的深蓝',                              'Apse Blue lives in the deepest part of the church where light barely reaches, the fresco there congealed into an unfading depth'),
        ('Vigil Blue',    '夜祷蓝是夜晚的色温——同一面壁画,在油灯下显现出一种与白日截然不同的暗蓝',                          'Vigil Blue is the night colour-temperature---the same wall, under oil lamp, reveals a dark blue utterly unlike its daytime self'),
        ('Crypt Blue',    '地宫蓝是壁画几乎被黑暗吞没的最深处,几近黑而仍属蓝——这是一组色彩中最沉默的「相信」',             'Crypt Blue is where the fresco is nearly swallowed by darkness, near black yet still blue---the most silent act of "believing" in the palette'),
    ]
))

# palette 8 — Monet
P.append(dict(
    num=8, name='Monet',
    philo_zh='印象派的核心命题是:光本身有颜色。莫奈一生反复画同一座干草堆、同一座大教堂、同一池睡莲,只为捕捉「同一个对象在不同时刻拥有不同色彩」的事实。这组配色不复刻任何一张莫奈作品,而是从他全部画作里抽出最具印象派身份的六个色相:奶油画布、玫瑰干草、绿草地、夏池水、晨雾蓝、深苇影——它们之间的关系不是构图,而是同一束光在不同物质上的折射。',
    philo_en='The central proposition of Impressionism is that light itself has colour. Monet painted the same haystack, the same cathedral, the same lily pond again and again across a lifetime, all to catch the fact that "the same object owns different colours at different hours". The palette reproduces no single Monet, but extracts from the body of his work six hues most diagnostic of Impressionist identity: creamy canvas, rose-touched hay, green meadow, summer pond, morning-mist blue, deep reed shadow---their relation is not composition but the refraction of one beam of light across different substances.',
    rows=[
        ((247,244,213), '画布奶油', 'Canvas Cream', 'Toile Cr\\`eme', '247, 244, 213', '莫奈打底未上色画布的奶油底', 'The creamy ground of an untouched Monet canvas'),
        ((211,150,140), '玫瑰干草', 'Hay Rose', 'Foin Rose', '211, 150, 140', '《干草堆》系列中黄昏时干草顶端的玫瑰', "The rose tipping the haystack in Monet\\'s evening series"),
        ((211,150,140), '夕辉粉', 'Evening Glow', 'Lueur du Soir', '211, 150, 140', '同色再现,延长黄昏的色温', 'Repeated, prolonging the colour-temperature of dusk'),
        ((131,153,88), '草地绿', 'Meadow Green', "Pr\\'e Vert", '131, 153, 88', '吉维尼花园午后草地的中调绿', 'The mid-green of the Giverny meadow in the afternoon'),
        ((16,86,102), '池水蓝', 'Pond Aqua', "\\'Etang Aigue", '16, 86, 102', '《睡莲》系列水面下倒映的深蓝', 'The deep blue mirrored beneath the water in the lily series'),
        ((10,51,35), '芦苇暗影', 'Reed Shadow', 'Ombre des Roseaux', '10, 51, 35', '池边芦苇丛根部的深绿,接近墨', 'The deep green at the base of the pondside reeds, near ink'),
    ],
    sub2_zh='印象派光色的色彩结构', sub2_en='Colour Structure of Impressionist Light',
    bullets=[
        ('Canvas Cream', '画布奶油是这组配色的「未完成」——是莫奈每一次起笔之前,画布本身的呼吸',                                'Canvas Cream is the palette\'s "unfinished"---the breath of the canvas itself before any of Monet\'s brush strokes'),
        ('Hay Rose',     '玫瑰干草是印象派最具识别性的一笔——它把「黄色」推向「玫瑰」,正是因为黄昏的光改写了一切固有色',         'Hay Rose is the most diagnostic Impressionist stroke---it pushes "yellow" into "rose" precisely because evening light has rewritten every local colour'),
        ('Evening Glow', '夕辉粉与玫瑰干草同色,是「延长黄昏」——印象派之所以反复画同一对象,正为多次捕捉这条色',                  'Evening Glow shares the hue of Hay Rose, the "prolonged dusk"---Impressionism returned to the same subject again and again precisely to catch this line of colour'),
        ('Meadow Green', '草地绿是配色的中调,是阳光打在新草上时的真实绿,既不冷也不暖',                                              'Meadow Green is the mid-tone of the palette, the true green of sunlight on new grass, neither cool nor warm'),
        ('Pond Aqua',    '池水蓝是莫奈晚年《睡莲》中最具识别性的色相,把蓝从天空借给水,是这组配色的情绪转折点',                      'Pond Aqua is the most diagnostic hue of late Monet\'s Water Lilies, lending blue from sky to water---the emotional pivot of the palette'),
        ('Reed Shadow',  '芦苇暗影是这组配色的「根」,几近墨而仍是绿——印象派的暗部从不真正接受黑',                                  'Reed Shadow is the root, nearly ink yet still green---Impressionism\'s shadows never truly accept black'),
    ]
))

# palette 9 — Narcissus
P.append(dict(
    num=9, name='Narcissus',
    philo_zh='不是希腊神话里的水仙,而是植物学意义上的水仙——一种从球根抽出花茎、在冬末春初开放的花。它的颜色谱系从苍白的鳞茎到金色的副冠、再到深褐的泥土根系,是一段「从地下到地面」的物质叙事。这组配色刻意去掉「绿叶」这一最显而易见的项,从而把视线集中在花本身从孕育、开放到回归大地的全过程,是一组以「时间纵轴」为结构的植物色谱。',
    philo_en='Not the Narcissus of Greek myth, but the botanical narcissus---a flower drawn from a bulb that opens at the close of winter. Its colour line runs from the pallid scale of the bulb to the gold of the corona and on to the deep brown of root in soil: a material narrative from underground to surface. The palette deliberately removes "green leaf", the most obvious element, so that the eye can focus on the flower\'s full arc---gestation, opening, return to earth---a botanical spectrum structured along the vertical axis of time.',
    rows=[
        ((221,213,200), '鳞茎乳', 'Bulb Milk', 'Bulbus Lacteus', '221, 213, 200', '刚切开的水仙球根截面的乳白', 'The milk-white of a freshly cut narcissus bulb in cross-section'),
        ((185,149,144), '花瓣粉褐', 'Petal Brown-Rose', 'Petalum Roseobrunneum', '185, 149, 144', '落瓣压在泥土里的灰玫瑰', 'A fallen petal pressed into soil, dust rose'),
        ((185,149,144), '退色玫瑰', 'Faded Rose', 'Rosa Defloruit', '185, 149, 144', '同色再现,代表「再用一次」的语义', 'The same colour returned---the "use it again" gesture'),
        ((199,149,72), '水仙金', 'Narcissus Gold', 'Aurum Narcissi', '199, 149, 72', '副冠中央的暖金,是配色的标识色', "The warm gold at the heart of the corona, the palette\\'s signal colour"),
        ((190,108,26), '蜂蜡铜', 'Honey Bronze', 'Aes Mellitum', '190, 108, 26', '球根外壳氧化后的橙褐,介于土与花之间', "The orange-brown of the bulb\\'s husk, sitting between soil and flower"),
        ((110,60,31), '泥土深', 'Soil Deep', 'Humus Profundus', '110, 60, 31', '水仙根系所在的腐殖土深褐,是根之色', 'The humus dark in which the narcissus roots, the colour of root'),
    ],
    sub2_zh='水仙生命周期的色彩切片', sub2_en='Colour Slices of a Narcissus Life Cycle',
    bullets=[
        ('Bulb Milk',        '鳞茎乳是水仙的「未开」,是植物在尚未成为花之前已经拥有的全部潜在颜色',                          'Bulb Milk is the narcissus before it opens---all the latent colour a plant already owns before it becomes flower'),
        ('Petal Brown-Rose', '花瓣粉褐是花的「凋落」,花瓣离开花茎后被泥土与雨水共同改写的颜色',                                'Petal Brown-Rose is the petal after the fall, the colour rewritten by soil and rain once it leaves the stem'),
        ('Faded Rose',       '退色玫瑰与花瓣粉褐同色,是「记忆中的同一片花瓣」——同一种凋落,在记忆里出现了第二次',           'Faded Rose shares its hue with Petal Brown-Rose---"the same fallen petal, remembered"---one falling, returning a second time in memory'),
        ('Narcissus Gold',   '水仙金是这组配色的核心,是副冠中央那一抹只在春天初醒时出现的暖金,是「开放」本身的颜色',         'Narcissus Gold is the core of the palette, the warm gold at the heart of the corona that appears only in early spring---the colour of "opening" itself'),
        ('Honey Bronze',     '蜂蜡铜把花的金推向了土的赭,是花朵从开放走向凋落、从空中回到地下的过渡色',                       'Honey Bronze pushes the flower\'s gold towards the earth\'s ochre---the transition from open flower to fallen petal, from air back to ground'),
        ('Soil Deep',        '泥土深是水仙的「来处」与「归处」,几近黑而保暖——这一组色彩告诉我们:任何盛开都从黑暗里来,也回去',  'Soil Deep is where the narcissus comes from and returns to, near black yet warm---the palette\'s closing argument that every blooming arrives from darkness and returns to it'),
    ]
))

# ===========================================================================
# palette 10 — Roman Empire
P.append(dict(
    num=10, name='Roman Empire',
    philo_zh='以罗马帝国的物质遗产为坐标:大理石、军团战袍、元老院托加、月桂冠、凯旋金、骨螺紫。六色不是设计而来,而是从罗马城本身长出来的——神庙的石、战场的血、广场的权、帝王的纹,共同构成一组配色的政治考古学。每一色都有可追溯的物质起源。',
    philo_en='A palette indexed by the material legacy of the Roman Empire: marble, legionary cloak, senatorial toga, laurel crown, triumphal gold, murex purple. The six tones are not designed but grown from the city of Rome itself---the stone of temples, the blood of battlefields, the authority of the forum, the mark of emperors---together forming a political archaeology of colour. Every shade has a traceable material origin.',
    rows=[
        ((236,232,225), '大理石', 'Carrara Marble', 'Marmor Carrariense', '236, 232, 225', '卡拉拉大理石的冷白,略带暖灰,是神庙与雕像的物质', 'The cool, faintly warm white of Carrara marble---the matter of temples and statues'),
        ((212,175,55), '荣耀金', 'Gloria Aurum', 'Aurum Gloriae', '212, 175, 55', '凯旋式黄金的中性金,介于铸币与神像镀金之间', 'A neutral gold of triumphal coinage, halfway between mint and idol'),
        ((74,110,65), '桂冠', 'Laurel Viridis', 'Laurus Viridis', '74, 110, 65', '月桂冠叶片的哑光深绿,取干燥叶片的沉稳色调', 'The matte deep green of the laurel crown, taken from dried leaves'),
        ((180,30,30), '罗马军团', 'Legion Crimson', 'Sagum Legionarium', '180, 30, 30', '军团战袍(Sagum)的鲜烈战红,饱和而有力,象征铁与血', 'The saturated red of the legionary sagum---iron, and blood'),
        ((120,20,40), '元老院', 'Senate Bordeaux', 'Clavus Senatorius', '120, 20, 40', '元老院托加袍缘的深沉酒红(Clavus),比军团红更内敛、更权贵', "The deeper wine of the senatorial toga\\'s clavus, restraint over force"),
        ((88,28,90), '奥古斯都紫', 'Tyrian Purple', 'Purpura Tyria', '88, 28, 90', '骨螺紫染料的历史色,价比黄金,专属皇权', 'Murex dye, worth its weight in gold, reserved for emperors'),
    ],
    sub2_zh='设计思路', sub2_en='Design Notes',
    bullets=[
        ('Carrara Marble',  '取自卡拉拉大理石的冷白底色,略带暖灰,呈现神庙与雕像的质感',                                       'Drawn from Carrara marble itself, a cool white with a faint warm grey, evoking the substance of temple and statue'),
        ('Legion Crimson',  '军团战袍(Sagum)的鲜烈战红,饱和而有力,象征铁与血',                                                  'The vivid battle-red of the legionary Sagum, saturated and forceful---a symbol of iron and blood'),
        ('Senate Bordeaux', '元老院托加袍缘的深沉酒红(Clavus),比军团红更内敛、更权贵',                                          'The deep wine red of the Clavus stripe on the senatorial toga, more restrained, more aristocratic than the legion\'s red'),
        ('Laurel Viridis',  '月桂冠叶片的哑光深绿,非翠绿,取干燥叶片的沉稳色调',                                                'The matte deep green of laurel leaves---not emerald, but the steady tone of the leaf once dried'),
        ('Gloria Aurum',    '凯旋式黄金的中性金,介于铸币与神像镀金之间,不过暖也不过冷',                                        'A neutral gold of triumphal procession, halfway between minted coin and gilded idol, neither overly warm nor cold'),
        ('Tyrian Purple',   '骨螺紫染料的历史色,价比黄金,专属皇权,深邃而神秘',                                                  'The historical dye drawn from murex shells, priced like gold, reserved for imperial use---deep, and arcane'),
    ]
))

# palette 11 — Greece
P.append(dict(
    num=11, name='Greece',
    philo_zh='以大理石白为底,民主蓝统领视觉重心,金色做高光点缀;陶器赤与橄榄绿构成一对冷暖平衡的中间调,葡萄紫作为最深的暗部锚点。大理石选用帕罗斯岛(Paros)产的暖白,比罗马卡拉拉更偏象牙,是帕特农神庙的实际用料;民主蓝取爱琴海深水区的中性蔚蓝,呼应雅典公民在广场(Agora)凝望的天与海。整体在地中海阳光下呈现出既庄重又充满生命力的古典张力。',
    philo_en='The marble is Parian, warmer and more ivory than Carrara, the actual material of the Parthenon; the democratic blue is taken from the mid-tone azure of the deep Aegean, the very sky and sea Athenians watched from the Agora. With marble as ground and democratic blue as the visual centre of gravity, gold accents, and terracotta-olive-grape as the three creative tones of narrative, wisdom and mystery.',
    rows=[
        ((245,240,228), '帕罗斯大理石', 'Parian Marble', '\\foreignname{Παριανός Μάρμαρος} \\textperiodcentered\\ Parianos Marmaros', '245, 240, 228', '帕特农神庙的实际用料,比卡拉拉更偏象牙的暖白', 'The actual stone of the Parthenon, warmer and more ivory than Carrara'),
        ((212,175,55), '荣耀金', 'Gloria Aurum', '\\foreignname{Χρυσός} \\textperiodcentered\\ Chrysos', '212, 175, 55', '与罗马同源的中性金,呼应神明与宗教仪式的高光', 'The same neutral gold as Rome, the highlight of gods and rite'),
        ((48,105,175), '民主蓝', 'Agora Kyanos', '\\foreignname{Κυανός Αγοράς} \\textperiodcentered\\ Kyanos Agoras', '48, 105, 175', '爱琴海深水区的中性蔚蓝,雅典公民在广场凝望的天与海', 'The mid-tone azure of the deep Aegean, the sky and sea Athenians watched from the Agora'),
        ((188,82,38), '陶器赤', 'Attic Terracotta', '\\foreignname{Αττικός Πηλός} \\textperiodcentered\\ Attikos Pelos', '188, 82, 38', '红绘式陶器的底色,希腊人记录神话与英雄史诗最具标志性的媒介色', 'The ground of red-figure pottery, the most iconic medium colour for recording myth and epic'),
        ((98,128,48), '橄榄银绿', "Athena's Olive", '\\foreignname{Ελιά Αθηνάς} \\textperiodcentered\\ Elia Athenas', '98, 128, 48', '雅典娜赠予城邦的橄榄树,和平与智慧的颜色', 'The olive tree gifted by Athena to the polis, the colour of peace and wisdom'),
        ((90,42,92), '狄俄尼索斯葡萄紫', 'Dionysian Grape', '\\foreignname{Διονυσιακή Σταφυλή} \\textperiodcentered\\ Dionysiake Staphyle', '90, 42, 92', '酿酒葡萄的深邃果紫,酒神、戏剧与狂欢节的灵魂色', 'The deep grape of wine-making, the soul colour of Dionysus, theatre, and revelry'),
    ],
    sub2_zh='配色逻辑', sub2_en='Colour Logic',
    bullets=[
        ('Parian Marble',     '大理石白作为底色,是希腊建筑与雕塑的物质本相——比罗马卡拉拉更暖、更象牙,带着地中海阳光过滤后的体温',           'Parian Marble as the ground is the material substrate of Greek architecture and sculpture---warmer and more ivory than Roman Carrara, carrying the body temperature of filtered Mediterranean sun'),
        ('Agora Kyanos',      '民主蓝统领整组色彩的视觉重心,既是爱琴海的天与海,也是雅典公民在广场上看见的「公共空间」的颜色',                  'Agora Kyanos commands the visual centre of gravity---both Aegean sky and sea, and the colour of "public space" Athenian citizens saw in the Agora'),
        ('Gloria Aurum',      '荣耀金作为点缀,以最小面积承担神圣与神明的视觉重量,与罗马同源却用法不同——希腊的金更克制',                       'Gloria Aurum, as accent, carries the visual weight of divinity in the smallest area---shared with Rome but used with more restraint here'),
        ('Attic Terracotta',  '陶器赤是希腊的「叙事色」——红绘陶器把神话与英雄史诗压在这一色里,是希腊文化最具识别性的媒介',                    'Attic Terracotta is the "narrative colour" of Greece---red-figure pottery pressed myth and epic into this one tone, the most diagnostic medium of Greek culture'),
        ("Athena's Olive",    '橄榄银绿与陶器赤构成冷暖平衡的中间调,是「智慧」与「叙事」的色彩对位',                                              'Athena\'s Olive and Attic Terracotta form a warm-cool mid-balance, a colour counterpoint of wisdom and narrative'),
        ('Dionysian Grape',   '葡萄紫是整组配色最深的暗部锚点,是酒神与戏剧的颜色——希腊文化的另一极:神圣之下的狂欢',                          'Dionysian Grape is the deepest anchor, the colour of Dionysus and theatre---the other pole of Greek culture: the revelry beneath the sacred'),
    ]
))

# palette 12 — Kanagawa (神奈川冲浪里)
P.append(dict(
    num=12, name='Kanagawa',
    philo_zh='《神奈川冲浪里》的革命性在于葛饰北斎将当时刚传入日本的普鲁士蓝(ベロ藍)引入浮世绘,以单一色系的深浅变奏构建出整幅画面的戏剧张力,配合墨线轮廓与富士山的远景留白,形成极具压缩感的视觉美学。这组配色以普鲁士蓝家族为核心,从墨黑→深海蓝→浪蓝→富士霞→暮天→波白构成一条完整的明度递进链,如同浪从深处涌起、在浪尖碎裂成雪沫的瞬间。',
    philo_en='The Great Wave\'s revolution lay in Hokusai\'s introduction of newly-imported Prussian blue (Bero-ai) into ukiyo-e: a single colour family in light-and-dark variation built the drama of the entire image, while ink outline and the distant blank of Mount Fuji produced a uniquely compressed visual aesthetic. The palette centres on the Prussian blue family---from sumi-ink to deep sea, to wave-blue, to Fuji-haze, to twilight sky, to foam-white---a complete luminance ladder, like a wave rising from the depths and bursting into snow at its crest.',
    rows=[
        ((237,233,222), '波白', 'Wave Foam', '\\foreignname{波白} \\textperiodcentered\\ Nami-shiro', '237, 233, 222', '浪尖破碎的泡沫,非纯白,带和纸的微暖底色', 'The foam at the cresting wave, not pure white but warmed by washi paper'),
        ((208,224,238), '暮天', 'Twilight Sky', '\\foreignname{暮天} \\textperiodcentered\\ Boten', '208, 224, 238', '海平线处的天空渐变色,普鲁士蓝淡化至苍茫', "The horizon sky\\'s gradient, Prussian blue diluted to vastness"),
        ((150,186,210), '富士霞', 'Fuji Haze', '\\foreignname{富士霞} \\textperiodcentered\\ Fuji-gasumi', '150, 186, 210', '远景富士山的淡蓝轮廓,虚化而沉静', 'The pale-blue silhouette of distant Mount Fuji, blurred and still'),
        ((26,78,132), '普鲁士蓝', 'Prussian Indigo', '\\foreignname{ベロ藍} \\textperiodcentered\\ Bero-ai', '26, 78, 132', '画面主体——普鲁士蓝浪身,江户最具标志性的舶来颜料', 'The main body of the image---the Prussian blue wave, the most iconic imported pigment of Edo'),
        ((13,38,76), '深海', 'Deep Sea', '\\foreignname{深海} \\textperiodcentered\\ Shinkai', '13, 38, 76', '浪底最深处的墨蓝,近乎黑而仍保有蓝的冷意', 'The ink-blue at the deepest trough of the wave, almost black yet keeping the chill of blue'),
        ((29,25,35), '墨', 'Sumi Ink', '\\foreignname{墨} \\textperiodcentered\\ Sumi', '29, 25, 35', '木版印刷的墨线,统摄全图骨架,非纯黑而含深紫底调', 'The ink line of woodblock print, the skeleton of the whole image, not pure black but with a deep violet base'),
    ],
    sub2_zh='配色逻辑', sub2_en='Colour Logic',
    bullets=[
        ('Nami-shiro',  '波白是浪尖那一瞬间的「破碎」,带和纸的微暖底色,是整组色彩唯一的高光',                                          'Nami-shiro is the instant of breaking at the crest, warmed by washi paper---the only highlight in the palette'),
        ('Boten',       '暮天是海平线处天空的过渡色,把普鲁士蓝淡化至几乎消失,是画面「呼吸」的色',                                      'Boten is the transitional sky at the horizon, Prussian blue diluted almost to vanishing---the colour the image breathes through'),
        ('Fuji-gasumi', '富士霞是远景富士山的淡蓝,是整幅画唯一的「退隐」,把焦点推回浪本身',                                              'Fuji-gasumi is the pale-blue distant Fuji, the single "retreat" in the painting, pushing focus back to the wave itself'),
        ('Bero-ai',     '普鲁士蓝是浪身的主色,是这幅画的革命所在——一种单一外来颜料,撑起了整幅作品的戏剧张力',                          'Bero-ai is the wave\'s body, the painting\'s revolution---a single imported pigment carrying the drama of the entire work'),
        ('Shinkai',     '深海是浪底最深处的墨蓝,是「压迫感」与「深渊」的色彩载体,近乎黑而仍是蓝',                                        'Shinkai is the ink-blue at the depth, the carrier of "pressure" and "abyss", almost black yet still blue'),
        ('Sumi',        '墨是木版印刷的骨架,统摄全图,是这组配色的「形」,没有它,六色蓝无可附着',                                          'Sumi is the skeleton of the woodblock, governing the whole image---the "form" of the palette, without which the six blues would have nothing to attach to'),
    ]
))

# palette 13 — Starry Night (星月夜)
P.append(dict(
    num=13, name='Starry Night',
    philo_zh='梵高的《星月夜》并非印象派而是后印象派的巅峰之作——他不再捕捉光的瞬间,而是将内心的情绪直接燃烧进笔触。画面以钴蓝与群青为骨,用漩涡状的笔触赋予夜空以生命,月光与星芒的铬黄在蓝色的重压下迸裂成光爆,柏树如黑色火焰直刺苍穹,村庄的微光则是整幅画中唯一属于人间的暖。三层蓝构成一条由深至浅的情绪纵深轴,模拟梵高螺旋笔触的叠压节奏。',
    philo_en='Van Gogh\'s Starry Night is not Impressionism but the summit of Post-Impressionism---he no longer catches the instant of light but burns the emotion inside directly into the brush stroke. Cobalt and ultramarine form the bone, the swirling stroke gives the night sky life, and the chrome yellow of moon and stars erupts under the weight of blue, while the cypress climbs like a black flame against the firmament; the village glow is the only warmth in the painting that belongs to the human world. Three layers of blue form an emotional axis from deepest to lightest, mimicking the layered rhythm of Van Gogh\'s spiral stroke.',
    rows=[
        ((240,208,68), '月华铬黄', 'Lunar Chrome', 'Lumi\\`ere Lunaire', '240, 208, 68', '月亮与星芒的爆裂光晕,梵高常用铬黄表达极致的生命张力', "The exploding halo of moon and starlight, Van Gogh\\'s chrome yellow as the utmost tension of life"),
        ((198,140,52), '村灯琥珀', 'Village Amber', 'Lueurs du Village', '198, 140, 52', '村庄窗口透出的暖黄,与冰冷蓝色星空形成全画唯一的冷暖对峙', 'The warm yellow from village windows, the only warm-cool stand-off against the cold blue sky'),
        ((105,155,200), '晨曦苍蓝', 'Glacial Dawn', "Aube Glac\\'ee", '105, 155, 200', '漩涡边缘的淡蓝过渡,深夜与月光交界处最微妙的呼吸感', "The pale-blue transition at the swirl\\'s edge, the most delicate breath between deep night and moonlight"),
        ((48,96,165), '星涡群青', 'Swirling Ultramarine', 'Tourbillon Outremer', '48, 96, 165', '漩涡主体的群青蓝,后印象派用色的标志——非自然色而是情绪色', "The ultramarine of the swirl\\'s body, the signature Post-Impressionist colour---not natural but emotional"),
        ((22,50,30), '柏影墨绿', 'Cypress Nocturne', 'Cypr\\`es Nocturne', '22, 50, 30', '前景柏树的深邃暗绿,几近于黑,是画面中唯一「拒绝光」的存在', 'The deep dark green of the foreground cypress, nearly black, the only thing in the painting that "refuses the light"'),
        ((20,36,88), '深夜钴蓝', 'Midnight Cobalt', 'Minuit Cobalt', '20, 36, 88', '夜空最深处的底色,饱含压迫性的情绪重量,梵高精神世界的深渊底色', "The deepest base of the night sky, dense with oppressive emotional weight---the abyss of Van Gogh\\'s inner world"),
    ],
    sub2_zh='配色逻辑', sub2_en='Colour Logic',
    bullets=[
        ('Lumi\\`ere Lunaire',  '月华铬黄是画面的「爆点」,月亮与星芒在蓝色重压下迸裂的光爆,是生命张力的极致',                  'Lumière Lunaire is the painting\'s "burst point", moon and stars exploding under the weight of blue---the very limit of life\'s tension'),
        ('Lueurs du Village',   '村灯琥珀是画中唯一属于人间的暖,与冰冷的蓝色星空构成全画唯一的冷暖对峙',                       'Lueurs du Village is the only earthly warmth in the painting, standing against the cold blue sky as the sole warm-cool counterpoint'),
        ('Aube Glac\\\'ee',     '晨曦苍蓝是过渡色,是深夜与月光交界处最微妙的呼吸感,介于压迫与解脱之间',                       'Aube Glacée is the transition, the most delicate breath between deep night and moonlight, between oppression and release'),
        ('Tourbillon Outremer', '星涡群青是漩涡主体,是后印象派用色的标志——非自然色而是情绪色,是这组配色的「主旋」',          'Tourbillon Outremer is the body of the swirl, the signature Post-Impressionist hue---not natural but emotional, the "melody line" of the palette'),
        ('Cypr\\`es Nocturne',  '柏影墨绿是画面唯一「拒绝光」的存在,几近于黑,是视觉锚点,以最暗的色撑起整幅画的对比',          'Cyprès Nocturne is the only element that "refuses the light", almost black---the visual anchor, holding up the contrast of the whole work with the darkest tone'),
        ('Minuit Cobalt',       '深夜钴蓝是夜空最深处的情绪底色,是梵高精神世界的深渊,所有蓝色由它生长而来',                    'Minuit Cobalt is the deepest emotional base of the night sky, Van Gogh\'s inner abyss, from which every other blue grows'),
    ]
))

# palette 14 — A Thousand Li (千里江山图)
P.append(dict(
    num=14, name='A Thousand Li',
    philo_zh='《千里江山图》由北宋王希孟以矿物颜料层层积染而成——石青、石绿研磨后反复叠压,非一次上色,而是以「薄中见厚」的积染工艺令色泽沉入绢底,形成一种由内向外透光的矿物质感。六色之间非独立存在,而是共同构成一套山水呼吸的色彩生态。',
    philo_en='A Thousand Li of Rivers and Mountains was painted by the Northern-Song prodigy Wang Ximeng with mineral pigments layered repeatedly---azurite and malachite ground fine and pressed coat upon coat, the "thin yet thick" technique sinking colour into the silk to give it a mineral translucence that glows from within outward. The six colours do not stand alone; together they form a colour ecology in which mountain and water breathe as one.',
    rows=[
        ((218,203,170), '宋绢暖', 'Song Silk', '\\foreignname{宋绢} \\textperiodcentered\\ S\\`ong-ju\\=an', '218, 203, 170', '千年绢素氧化后的暖米底色,非颜料而是时间本身的色彩', 'The warm rice ground of millennia-aged silk, not pigment but the colour of time itself'),
        ((110,165,195), '烟渚色', 'Sky Azurite', '\\foreignname{烟渚} \\textperiodcentered\\ Y\\=an-zh\\v{u}', '110, 165, 195', '石青与铅白调和后的淡化层,用于远山轮廓与江面折光', 'The diluted layer of azurite and lead white, used for distant mountain silhouette and river highlights'),
        ((183,118,45), '砂岩赭', 'Ochre-Gold', '\\foreignname{砂赭} \\textperiodcentered\\ Sh\\=a-zh\\v{e}', '183, 118, 45', '赭石(褐铁矿)与泥金混调,用于勾勒礁石肌理、屋舍廊桥与水波金线', 'Ochre limonite mixed with mud-gold, used for reef texture, dwelling, gallery bridge, and gold lines on water'),
        ((96,148,110), '岚霭绿', 'Pale Malachite', '\\foreignname{岚霭绿} \\textperiodcentered\\ L\\\'an-\\v{a}i-l\\"u', '96, 148, 110', '石绿渐次减量后的过渡色,表现中景植被与山腰云雾交融处', 'The transitional tone of progressively diluted malachite, the mid-ground foliage and the cloud-mountain interface'),
        ((48,105,76), '苍岭绿', 'Malachite True', '\\foreignname{苍岭绿} \\textperiodcentered\\ C\\=ang-l\\v{i}ng-l\\"u', '48, 105, 76', '天然孔雀石的正色,层叠于山峦受光面,画面最具生命感的色调', 'The true colour of natural malachite, layered on sunlit mountain faces, the most life-bearing tone of the painting'),
        ((35,78,112), '霁山青', 'Azurite Deep', '\\foreignname{霁山青} \\textperiodcentered\\ J\\`i-sh\\=an-q\\=ing', '35, 78, 112', '天然蓝铜矿研细后的深沉矿蓝,画中山体背阴面与水深处的主色', "The deep mineral blue of finely-ground azurite, the dominant tone of the mountain\\'s shaded face and deep water"),
    ],
    sub2_zh='五大特征的色彩映射', sub2_en='Colour Mapping of the Five Characteristics',
    bullets=[
        ('青绿主调',       '霁山青与苍岭绿共同锚定全组色彩的主旋,一冷一暖,一阴一阳,相互制衡而非竞争',                    'Azure-and-Green Lead: Azurite Deep and Malachite True jointly anchor the main key---one cool one warm, one yin one yang, each balancing rather than competing with the other'),
        ('层次渐变',       '从霁山青→烟渚色、苍岭绿→岚霭绿,各形成一条明度递进链,模拟积染工艺的「薄中见厚」',           'Gradient Layering: from Azurite Deep to Sky Azurite, from Malachite True to Pale Malachite---each line is a luminance ladder, mimicking the layered technique of "thin yet thick"'),
        ('金赭点缀',       '砂岩赭以最小的面积承担最大的温度调节职责,令青绿主调不至于流于清冷',                            'Gold-Ochre Accent: Ochre-Gold takes on the largest duty of temperature adjustment in the smallest area, keeping the azure-green lead from slipping into chill'),
        ('空灵雅致',       '烟渚色与岚霭绿的介入,在浓重矿色之间打开呼吸的空间,令整组色不堵不闷',                          'Ethereal Refinement: Sky Azurite and Pale Malachite open breath between the dense mineral tones, so the whole palette neither clogs nor stifles'),
        ('古绢质感',       '宋绢暖作为底色托起五色,如同千年绢素将所有浓烈都沉淀为一种悠远的克制',                          'Antique Silk Quality: Song Silk holds the five tones, the way millennia-aged silk settles every intensity into a far, restrained tone'),
    ]
))

# palette 15 — And Quiet Flows the Don (静静的顿河)
P.append(dict(
    num=15, name='And Quiet Flows the Don',
    philo_zh='肖霍洛夫用二十年写完这部史诗,顿河哥萨克的命运从不在鲜亮之处——它埋在冻土里、锈在马刀上、凝在战壕边的黑血里、散在大雪漫过的苇荡中。这组配色拒绝一切「颜色」,只留下时间磨损之后的残余:不是蓝,是浊蓝;不是红,是暗血;不是黄,是枯草;不是灰,是铅灰。',
    philo_en='Sholokhov spent twenty years writing this epic. The fate of the Don Cossacks never lives in the bright places---it is buried in frozen earth, rusted onto sabres, congealed in the black blood at the trench, scattered through reed marshes the snow has crossed. This palette refuses every "colour" and keeps only what time leaves after wearing them down: not blue but turbid blue, not red but dark blood, not yellow but withered grass, not grey but lead grey.',
    rows=[
        ((142,120,70), '枯苇秋黄', 'Wormwood Yellow', '\\foreignname{Полынь} \\textperiodcentered\\ Polyn', '142, 120, 70', '顿河边被霜打过的苇草与苦艾,褪色的黄绿', 'Reeds and wormwood by the Don after the first frost, a withered yellow-green'),
        ((110,108,104), '草原铅灰', 'Steppe Lead Grey', '\\foreignname{Степной Пепел} \\textperiodcentered\\ Stepnoy Pepel', '110, 108, 104', '冬日荒原的天与地混为一色,哥萨克男人眼神里的那种灰', "The winter steppe where sky and ground merge into one tone, the very grey of a Cossack man\\'s gaze"),
        ((118,86,52), '黄土大地', 'Don Earth', '\\foreignname{Донская Земля} \\textperiodcentered\\ Donskaya Zemlya', '118, 86, 52', '顿河流域特有的栗钙土,带腐殖质气息的褐色', 'The chestnut soil unique to the Don basin, brown with the smell of humus'),
        ((122,66,36), '铁锈赭红', 'Rusted Iron', '\\foreignname{Ржавое Железо} \\textperiodcentered\\ Rzhavoye Zhelezo', '122, 66, 36', '哥萨克军刀、马镫、步枪枪托上的锈蚀,战争腐蚀金属的颜色', 'The rust on sabre, stirrup, and rifle stock---the colour of war corroding metal'),
        ((52,70,90), '顿河浊蓝', 'Don Muddy Blue', '\\foreignname{Мутный Дон} \\textperiodcentered\\ Mutnyy Don', '52, 70, 90', '顿河从不清澈——裹挟泥沙与战死者的血,全书的时间底色', 'The Don is never clear---it carries silt and the blood of the slain, the time-base of the whole novel'),
        ((88,26,24), '暗血战痕', 'Caked Blood', '\\foreignname{Запёкшаяся Кровь} \\textperiodcentered\\ Zapyokshayasya Krov', '88, 26, 24', '凝固三日后渗入军衣的深褐红,血色命运在这里沉默', 'The deep brown-red that seeps into uniform three days after a wound---blood as fate, silenced'),
    ],
    sub2_zh='色彩结构的悲剧逻辑', sub2_en='Tragic Logic of the Colour Structure',
    bullets=[
        ('冷灰压顶',  '草原铅灰与顿河浊蓝构成整组色彩的天空与水面,将所有暖色死死压在下方,如同历史对个体命运的碾压从未松手', 'Cold Grey Holds the Lid: Steppe Lead Grey and Don Muddy Blue press every warm tone beneath them, as history\'s grinding of individual fate has never let go'),
        ('土褐承重',  '黄土大地与枯苇秋黄是这片土地仅剩的「生」意,但它们同样去饱和、去鲜亮,美也是疲惫的美',                 'Earth Tones Bear the Weight: Don Earth and Wormwood Yellow are the only "living" still left to this land, but desaturated and dulled---even beauty is tired beauty'),
        ('暗血锚底',  '暗血战痕是全组最深的极色,不做主角,只在最沉的阴影处出现——如同《静静的顿河》里的死亡,从不戏剧化',     'Dark Blood Anchors the Floor: Caked Blood is the deepest extremity, never the protagonist, appearing only in the heaviest shadow---like death in this novel, never dramatised'),
        ('锈感贯穿',  '铁锈赭红横跨土褐与暗血之间,是这组配色的「时间感」载体,它告诉观者:这里所有的一切,都已经过去很久了', 'Rust Threads Through: Rusted Iron crosses between earth-brown and dark blood, the carrier of "time-sense"---telling the viewer that all of this has already been long past'),
    ]
))

# palette 16 — Cyberpunk Edgerunners (赛博朋克边缘行者)
P.append(dict(
    num=16, name='Cyberpunk Edgerunners',
    philo_zh='《边缘行者》的视觉语言本质是过载美学——色彩不是装饰,是症状。大卫的精神崩溃伴随着荧光色彩的失控侵蚀,夜之城的霓虹不是繁荣的象征而是麻醉剂,Lucy 的蓝是这个世界里唯一真实的出口。这组配色的核心矛盾是:极暗的底色与极亮的荧光并置,产生几近生理不适的振动感。',
    philo_en='The visual language of Edgerunners is overload aesthetics in essence---colour here is not ornament but symptom. David\'s breakdown comes with the runaway erosion of fluorescent tones; the neon of Night City is not the sign of prosperity but an anaesthetic; Lucy\'s blue is the only real exit this world owns. The central contradiction of the palette is this: the darkest possible base set against the most fluorescent possible highlight, producing a vibration close to bodily discomfort.',
    rows=[
        ((225,255,8), '迷幻荧黄', 'Psycho Yellow', '\\foreignname{サイコ黄} \\textperiodcentered\\ Saiko-ki', '225, 255, 8', '大卫夹克的灵魂色,赛博精神病发作时视觉过载之色', "The soul colour of David\\'s jacket, the visual overload at the onset of cyberpsychosis"),
        ((10,238,100), '电路荧绿', 'Flatline Green', '\\foreignname{電脳緑} \\textperiodcentered\\ Dennō-ryoku', '10, 238, 100', '网络骇入的代码流与改造体的皮下光纹', 'The code stream of network intrusion and the subdermal light tracery of chromed bodies'),
        ((238,18,120), '霓虹品红', 'Neon Magenta', '\\foreignname{ネオン桃} \\textperiodcentered\\ Neon-momo', '238, 18, 120', '夜之城最泛滥的霓虹,繁荣谎言的颜色', "The most overflowing neon of Night City, the colour of prosperity\\'s lie"),
        ((205,20,35), '鲜血赤红', 'Edgerunner Red', '\\foreignname{エッジ赤} \\textperiodcentered\\ Edge-aka', '205, 20, 35', '边缘行者的代价,街头枪战后水泥地上的颜色', 'The price an edgerunner pays, the colour on the concrete after a street firefight'),
        ((15,32,98), '露娜深蓝', 'Luna Blue', '\\foreignname{月の蒼} \\textperiodcentered\\ Tsuki-no-ao', '15, 32, 98', 'Lucy 仰望月球的眼神,唯一不属于夜之城的颜色', 'Lucy looking up at the moon---the only colour that does not belong to Night City'),
        ((14,8,28), '夜都虚空', 'Night City Void', '\\foreignname{夜都虚空} \\textperiodcentered\\ Yato Kokū', '14, 8, 28', '夜之城街道底层的绝对黑暗,含深紫底调', "The absolute darkness at the floor of Night City\\'s street, carrying a deep violet undertone"),
    ],
    sub2_zh='色彩结构的叙事逻辑', sub2_en='Narrative Logic of the Colour Structure',
    bullets=[
        ('虚空压底',    '夜都虚空作为绝对底色,饱和度趋近于零,是让其余五色得以「爆炸」的必要前提。没有黑暗,霓虹只是颜料',         'Void Holds the Floor: Night City Void is the absolute ground, with saturation near zero, the precondition that lets the other five "explode". Without darkness, neon is only pigment'),
        ('冷暖裂变',    '露娜深蓝与霓虹品红、迷幻荧黄构成最极端的冷暖对立:蓝是 Lucy 的月球梦,粉与黄是夜之城的谎言与疯狂',         'Cold/Warm Rupture: Luna Blue against Neon Magenta and Psycho Yellow forms the most extreme warm-cool opposition---blue is Lucy\'s lunar dream; pink and yellow are the lies and madness of Night City'),
        ('荧光过载',    '迷幻荧黄与电路荧绿是赛博精神病美学的视觉核心,两色并置时产生几近生理不适的振动感',                          'Fluorescent Overload: Psycho Yellow and Flatline Green are the visual core of cyberpsychosis aesthetics; placed side by side they produce a vibration close to bodily discomfort'),
        ('红色终章',    '鲜血赤红在色板中不做主角,却是最诚实的颜色——像结局一样,无可回避',                                            'Red Finale: Edgerunner Red is not the protagonist in the plate, but the most honest colour---like the ending, impossible to avoid'),
    ]
))

# palette 17 — The Grand Budapest Hotel (布达佩斯大饭店)
P.append(dict(
    num=17, name='The Grand Budapest Hotel',
    philo_zh='韦斯·安德森的配色从不是写实的,而是经过精密校准的情感滤镜——《布达佩斯大饭店》的粉色不是粉色,是一整个正在消逝的旧欧洲贵族世界被压缩成的颜色;紫色不是紫色,是古斯塔夫先生永不失礼的最后尊严。每一种颜色都经过刻意的去真实化处理。',
    philo_en='Wes Anderson\'s colour is never realist---it is a precisely calibrated emotional filter. The pink of The Grand Budapest Hotel is not pink; it is the colour of an entire vanishing old-European aristocratic world compressed into a single tone. The purple is not purple; it is Monsieur Gustave\'s final, never-impolite dignity. Every shade has been deliberately de-realised.',
    rows=[
        ((247,235,215), '香草奶油', 'Vanilla Cream', 'Cr\\`eme Vanille', '247, 235, 215', '饭店内壁、Mendl 蛋糕胚、信笺底色,童话世界的空气本身', "Hotel interior, Mendl\\'s sponge, letter paper---the very air of a fairy-tale world"),
        ((168,178,196), '阿尔卑斯雾蓝', 'Alpine Mist', 'Brume Alpine', '168, 178, 196', '积雪山景、冬日车厢窗外的低饱和冷调,情绪降温剂', 'Snowy alps, the desaturated cool outside a winter coach---the emotional refrigerant'),
        ((237,148,158), '美酒蔷薇', "Mendl's Rose", "Rose M\\'endl", '237, 148, 158', '饭店外墙与 Mendl 甜品盒的标志粉,掺了一丝尘埃的旧玫瑰色', "The signature pink of the hotel façade and Mendl\\'s confectionery box, a dust-touched old rose"),
        ((176,136,60), '古铜暗金', 'Antique Gold', "Dor\\'e Antique", '176, 136, 60', '镀金镜框、门把手、制服肩章的年岁感,旧贵族的光泽', 'Gilded mirror frame, doorknob, shoulder braid---the patina of old aristocracy'),
        ((128,88,148), '执行者紫', 'Concierge Violet', 'Violet Concierge', '128, 88, 148', '古斯塔夫先生制服的紫,兼具权威与荒诞', "The purple of Monsieur Gustave\\'s uniform, at once authority and absurdity"),
        ((143,52,65), '复古酒绛', 'Vintage Bordeaux', 'Bordeaux Vintage', '143, 52, 65', '深色场景的戏剧性锚点——图书馆皮革、红酒、密谋与危险', 'The dramatic anchor of dark scenes---library leather, claret, conspiracy and danger'),
    ],
    sub2_zh='五重美学法则的色彩映射', sub2_en='Colour Mapping of the Five Aesthetic Rules',
    bullets=[
        ('马卡龙柔色', '蔷薇粉与执行者紫是主视觉担当,高饱和但经过刻意的明度压制,像马卡龙饼壳——色彩分明却绝不刺眼',           'Macaron Softness: Rose Méndl and Violet Concierge carry the main visual, high saturation deliberately tamed in luminance---like the shell of a macaron, distinct yet never glaring'),
        ('奶油暖底',   '香草奶油以最大留白统摄全局,是韦斯·安德森式对称构图里的「负空间」,令其他五色不至于拥挤',               'Cream Warm Ground: Crème Vanille rules through the largest negative space, the "void" of Wes Anderson\'s symmetric composition---keeping the other five from crowding'),
        ('复古暗金',   '古铜暗金专门负责「贵族感」的重量,它不参与童话叙事,只在边框与细节处发光',                                   'Antique Dark Gold: Doré Antique carries the weight of "aristocracy", taking no part in the fairy-tale narrative---glowing only in frame and trim'),
        ('冷调克制',   '阿尔卑斯雾蓝是全组唯一的冷色,低饱和度让它成为调节器,在甜腻的暖色系中打开一扇透气的窗',                   'Cool Restraint: Brume Alpine is the only cool, its low saturation making it the regulator, opening a window of breath inside an otherwise sweet warm field'),
        ('甜而不腻',   '复古酒绛是整组配色最精妙的设计:一粒深沉的暗色锚点,像甜点里的一滴苦杏仁酒,让所有的轻盈都有了重量',       'Sweet Without Cloy: Bordeaux Vintage is the most subtle move---a deep dark anchor, the drop of amaretto inside the dessert, giving every lightness its weight'),
    ]
))

# palette 18 — Renaissance Florence (文艺复兴佛罗伦萨)
P.append(dict(
    num=18, name='Renaissance Florence',
    philo_zh='佛罗伦萨的色彩并非设计而来,而是从物质本身生长出来的——青金石研磨成颜料、铅白调入蛋黄成坦培拉底料、金箔贴于木质祭坛、陶土在托斯卡纳窑火中烧成穹顶砖瓦。这六种颜色皆有真实的物质出处:它们曾是颜料、矿石、建材、木料,是波提切利、乔托与多纳泰罗共同呼吸的色谱。',
    philo_en='The colour of Florence was not designed but grew out of substance itself---lapis lazuli ground into pigment, lead white folded with yolk into tempera ground, gold leaf laid on wooden altar, terracotta fired in the Tuscan kiln into dome tile. All six of these colours have a real material provenance: they were once pigment, ore, building stone, and timber---the spectrum Botticelli, Giotto, and Donatello breathed together.',
    rows=[
        ((238,228,208), '翡冷翠象牙', 'Florentine Ivory', 'Avorio Fiorentino', '238, 228, 208', '卡拉拉大理石截面与坦培拉画板的打底铅白,含蛋黄与亚麻油的暖意', 'The lead-white ground of cut Carrara marble and tempera panel, warmed by yolk and linseed'),
        ((190,148,52), '祭坛暖金', 'Altar Gold', "Oro dell'Altare", '190, 148, 52', '圣母像背光与美第奇金饰的金箔色,五百年空气氧化后内敛发光的旧金', "The gold leaf of the Madonna\\'s nimbus and Medici ornament, an aged gold still glowing after five centuries of oxidation"),
        ((172,84,50), '穹顶陶红', 'Brunelleschi Cotto', 'Cotto Brunellesco', '172, 84, 50', '布鲁内莱斯基穹顶砖瓦与佛罗伦萨屋檐的标志陶土红', "The signature terracotta of Brunelleschi\\'s dome and Florentine eaves"),
        ((54,80,60), '柏影墨绿', 'Cypress Verde', 'Verde Cipresso', '54, 80, 60', '托斯卡纳丘陵柏树与铜绿颜料(Verdigris)的混调', 'The cypress and verdigris mix of the Tuscan hill'),
        ((46,70,118), '青金矿蓝', 'Lapis Ultramarine', 'Oltremare di Lapislazzuli', '46, 70, 118', '产自阿富汗矿山的青金石研磨所得,价比黄金,专用于圣母袍服', "Ground from Afghan lapis lazuli, priced like gold, reserved for the Madonna\\'s robe"),
        ((85,54,34), '胡桃深褐', 'Tuscan Walnut', 'Noce Toscano', '85, 54, 34', '佛罗伦萨工坊核桃木画板与深色底釉的颜色', 'The walnut panel and dark underglaze of the Florentine workshop'),
    ],
    sub2_zh='四重气质的色彩映射', sub2_en='Colour Mapping of the Four Temperaments',
    bullets=[
        ('神圣庄重', '青金矿蓝承担全组的精神重量。青金石在文艺复兴时期价比黄金,非普通委托可用,它的存在本身即是神圣的声明;祭坛暖金以最克制的方式散发光晕,二者共同构建宗教艺术的仪式感', 'Sacred Solemnity: Oltremare carries the spiritual weight of the whole set. In the Renaissance, lapis was priced like gold and not available to common commission---its very presence is a sacred declaration; Oro dell\'Altare lets out its glow in the most restrained way, and the two together build the rite of religious art'),
        ('温润华贵', '翡冷翠象牙与祭坛暖金是贵族底色的两面——一个是触感温润的大理石与绢布,一个是美第奇家族以财富供养艺术的金属记忆;陶土红以人间温度调和神圣的冷峻',                                'Warm Nobility: Avorio Fiorentino and Oro dell\'Altare are the two faces of the aristocratic ground---one the warm touch of marble and silk, the other the Medici memory of wealth feeding art; Cotto Brunellesco then tempers sacred austerity with human warmth'),
        ('古典醇厚', '六色均经过刻意的去现代化处理:无一纯色,皆含矿物杂质的「不纯粹」——这正是天然颜料与合成色料最根本的区别。厚重来自饱和度的克制,醇厚来自每个颜色内部的复杂性',         'Classical Depth: All six tones are deliberately de-modernised, no pure colour anywhere, each carrying the "impurity" of mineral debris---this is the most fundamental difference between natural pigment and synthetic dye. Heft comes from restrained saturation, depth from each colour\'s inner complexity'),
        ('人文雅致', '柏影墨绿与胡桃深褐是人文主义的色彩锚点:绿来自托斯卡纳的自然山丘,褐来自工坊的核桃木画板,它们将神圣从天空拉回大地',                                                            'Humanist Refinement: Verde Cipresso and Noce Toscano are the humanist anchors of the palette---the green comes from the natural Tuscan hill, the brown from the walnut panel of the workshop; together they pull the sacred from sky back to earth'),
    ]
))

# palette 19 — Soviet Avant-Garde (苏联先锋主义)
P.append(dict(
    num=19, name='Soviet Avant-Garde',
    philo_zh='苏联先锋派从不「设计配色」——他们宣告颜色。罗钦科说色彩必须有任务,李西茨基说形式即政治,马列维奇说至上主义的黑色正方形是零度的绝对。这组配色拒绝调和、拒绝渐变、拒绝装饰性的过渡,每种颜色都是一个硬边宣言:红色不解释自己,黑色不道歉,灰色不讨好任何人。',
    philo_en='The Soviet avant-garde never "designed" colour---they declared it. Rodchenko said colour must have a task; Lissitzky said form is politics; Malevich said the Suprematist black square is the absolute of zero. This palette refuses harmony, refuses gradient, refuses the decorative transition: every colour is a hard-edged manifesto. Red does not explain itself, black does not apologise, grey does not curry favour with anyone.',
    rows=[
        ((225,218,205), '粗纸白', 'Newsprint White', '\\foreignname{ГАЗЕТА} \\textperiodcentered\\ Gazeta', '225, 218, 205', '《真理报》与构成主义宣传册的新闻纸白,含油墨渗透后的暖灰底调', 'The newspaper white of Pravda and constructivist brochures, an ink-soaked warm grey'),
        ((200,150,32), '宣传赭黄', 'Propaganda Ochre', '\\foreignname{ПЛАКАТ} \\textperiodcentered\\ Plakat', '200, 150, 32', '克鲁齐斯摄影蒙太奇海报与农业集体化宣传画的赭黄', 'The ochre of Klutsis photomontage poster and collectivisation propaganda print'),
        ((118,114,108), '混凝土灰', 'Concrete Grey', '\\foreignname{БЕТОН} \\textperiodcentered\\ Beton', '118, 114, 108', '塔特林塔、莫斯科工厂厂房、五年计划基建工地的浇筑混凝土色', "The poured concrete of Tatlin\\'s Tower, Moscow factory, and Five-Year-Plan worksite"),
        ((50,80,138), '机械蓝', 'Blueprint Blue', '\\foreignname{ЧЕРТЁЖ} \\textperiodcentered\\ Chertyozh', '50, 80, 138', '工程蓝图与苏联工人阶级制服的冷蓝,去饱和处理', 'The blueprint blue of the working-class uniform, deliberately desaturated'),
        ((196,28,28), '列宁红', 'Lenin Red', '\\foreignname{КРАСНЫЙ} \\textperiodcentered\\ Krasnyy', '196, 28, 28', '布尔什维克旗帜与罗钦科海报的革命红,刻意压低饱和度令其沉重如铁', 'The revolutionary red of the Bolshevik flag and Rodchenko poster, pressed down in saturation to weigh like iron'),
        ((24,20,18), '铸铁黑', 'Cast-Iron Black', '\\foreignname{ЧЁРНЫЙ} \\textperiodcentered\\ Chyornyy', '24, 20, 18', '马列维奇《黑色正方形》的绝对黑,虚无与确定性同时存在的黑', "The absolute black of Malevich\\'s Black Square, where nothingness and certainty coexist"),
    ],
    sub2_zh='六重美学法则的色彩映射', sub2_en='Colour Mapping of the Six Aesthetic Rules',
    bullets=[
        ('红黑强撞',       '列宁红与铸铁黑是整组配色的结构核心,二者之间无过渡、无缓冲,直接对撞——对比本身即是论点',                                          'Red-Black Hard Strike: КРАСНЫЙ and ЧЁРНЫЙ are the structural core, with no transition and no buffer between them---contrast itself is the argument'),
        ('工业灰的中轴',   '混凝土灰不参与任何戏剧,它只是站在那里承重,如同五年计划中那些无名工人,是这组配色的脊柱而非焦点',                                'Industrial Grey Axis: БЕТОН takes part in no drama, it merely stands and bears the load---like the nameless workers of the Five-Year-Plan, the spine, not the focus'),
        ('机械蓝的精确',   '机械蓝刻意压低至近乎去色的状态,与列宁红形成冷暖的意识形态对立:红是革命的激情,蓝是建设的纪律',                                'Mechanical Blue Precision: ЧЕРТЁЖ is pressed nearly to colourlessness, forming an ideological warm-cool opposition with КРАСНЫЙ---red the passion of revolution, blue the discipline of construction'),
        ('粗纸白的民主性', '新闻纸白是这组配色里唯一的「反精英」色,它拒绝象牙白的贵族温润,选择廉价印刷品的粗糙质感',                                    'Democratic Coarse White: ГАЗЕТА is the only "anti-elite" tone, refusing the aristocratic warmth of ivory and choosing the coarseness of cheap print'),
        ('赭黄的未竟性',   '宣传赭黄是全组配色中最具悲剧性的颜色:它是海报上的丰收麦穗、是乌托邦宣传画里永远灿烂的明天,是一个承诺的颜色而非现实的颜色',  'Unkept Ochre: ПЛАКАТ is the most tragic tone, the colour of poster wheat and forever-sunlit utopian tomorrows---a colour of promise, not of reality'),
    ]
))

# palette 20 — Constantinople (君士坦丁堡)
P.append(dict(
    num=20, name='Constantinople',
    philo_zh='君士坦丁堡是人类历史上唯一一座同时属于两个大陆、三种文明、四种宗教的城市——它的颜色从不单纯。圣索菲亚大教堂的穹顶金光里叠压着希腊工匠、罗马工程、东方神学;博斯普鲁斯海峡的深蓝里混着黑海的寒流与爱琴海的温暖;帝王紫是用地中海骨螺提炼出的奢华。',
    philo_en='Constantinople is the only city in human history to belong, all at once, to two continents, three civilisations, and four religions---its colours are never simple. The gold of Hagia Sophia\'s dome holds Greek craft, Roman engineering, and Eastern theology in superposition. The deep blue of the Bosporus mixes the Black Sea\'s chill with the Aegean\'s warmth. The imperial purple is luxury distilled from Mediterranean murex.',
    rows=[
        ((236,225,207), '普罗科尼索象牙', 'Proconnesian Ivory', '\\foreignname{Λευκός} \\textperiodcentered\\ Fildi\\c{s}i', '236, 225, 207', '马尔马拉海小岛出产的普罗科尼索大理石,铺满圣索菲亚内殿地面', 'Marble of the Sea of Marmara, the floor of Hagia Sophia'),
        ((195,150,42), '圣索菲亚金', 'Hagia Sophia Gold', '\\foreignname{Χρυσός} \\textperiodcentered\\ Alt\\i n', '195, 150, 42', '圣索菲亚穹顶马赛克金箔的光,一千五百年烛烟熏染后内敛发光的旧金', 'The aged gold smoked by fifteen centuries of candles, sacred and unshowy'),
        ((170,112,50), '狄奥多西赭', 'Theodosian Ochre', "\\foreignname{\\'{Ω}χρα} \\textperiodcentered\\ Toprak", '170, 112, 50', '狄奥多西城墙砖石与博斯普鲁斯岸边老建筑的赭土色', 'The brick of the Theodosian Walls, the shared ground of Greek, Roman, Anatolian'),
        ((50,76,58), '柏树暗绿', 'Cypress Dark Green', '\\foreignname{Κυπαρίσσι} \\textperiodcentered\\ Selvi', '50, 76, 58', '君士坦丁堡山丘柏树与拜占庭绿色斑岩柱础的深沉暗绿', 'Byzantine cemetery and Islamic garden---two faiths watching the same eternity'),
        ((102,32,65), '帝王骨螺紫', 'Imperial Murex', '\\foreignname{Πορφύρα} \\textperiodcentered\\ Mor', '102, 32, 65', '拜占庭皇帝专属的骨螺紫,提炼一克需杀万只骨螺', 'Restricted to the Byzantine emperor: a single gram demands ten thousand murex shells'),
        ((30,52,88), '博斯普鲁斯蓝', 'Bosporus Blue', '\\foreignname{Βόσπορος} \\textperiodcentered\\ Bo\\u{g}az', '30, 52, 88', '海峡傍晚收拢光线后的深沉蓝,黑海与爱琴海在此交汇', 'The deep blue of the strait at dusk, where the Black Sea meets the Aegean'),
    ],
    sub2_zh='文明交汇的色彩结构', sub2_en='The Colour Structure of Civilisations in Confluence',
    bullets=[
        ('东西冷暖轴',    '博斯普鲁斯深蓝(西方理性、海洋秩序)与狄奥多西赭(东方大地、安纳托利亚土壤)构成配色的东西文明轴线;二者温度相反,却在君士坦丁堡这座城市里共存了千年而未曾消解', 'East-West Warm/Cool Axis: Bosporus blue (Western reason, maritime order) and Theodosian ochre (Eastern earth, Anatolian soil) form the East-West civilisational axis---opposite in temperature, they coexisted for a millennium without dissolving in this city'),
        ('神圣三角',      '圣索菲亚金、帝王骨螺紫、普罗科尼索象牙共同构建宗教神圣感的色彩空间:金是神的光,紫是神在人间的代理人,象牙是神居住其中的建筑肌肤',                              'Sacred Triangle: Hagia Sophia gold, imperial purple, Proconnesian ivory together build the colour space of the sacred---gold is the light of God, purple is God\'s human agent, ivory is the architectural skin in which God resides'),
        ('紫红的文明桥接','帝王骨螺紫在整组配色中承担最复杂的角色:它同时属于罗马帝国的皇权传统、拜占庭基督教的神学色彩,以及波斯-东方宫廷的奢华美学',                                    'Purple as Civilisational Bridge: Imperial Murex bears the most complex role in the whole set, belonging at once to Roman imperial tradition, Byzantine Christian theology, and Persian-Eastern court luxury'),
        ('暗绿的历史纵深','柏树暗绿以最低调的姿态承载最漫长的时间跨度:它同时出现在拜占庭墓地柏树、奥斯曼庭园绿化与伊斯兰清真寺的铜绿穹顶上',                                              'Dark Green Holds Deep Time: Cypress dark green carries the longest time span in the most low-key form---present at once in Byzantine cemetery cypress, Ottoman garden, and the verdigris dome of the mosque'),
        ('金辉内敛',      '整组配色刻意将圣索菲亚金的饱和度压低至矿物感区间,令其发光而不炫目——这是拜占庭马赛克艺术的核心逻辑:金不是装饰,是光本身的物质化',                              'Restrained Gold: The palette deliberately compresses Hagia Sophia gold into mineral-tone saturation, glowing without glare---this is the central logic of Byzantine mosaic: gold is not ornament but the materialisation of light'),
    ]
))

# palette 21 — France (法兰西)
P.append(dict(
    num=21, name='France',
    philo_zh='法国的颜色从不是单纯的颜色——它是一种世界观的物质显现。共和红里藏着断头台与玫瑰,深蓝里住着笛卡尔的理性与莫奈的晨雾,香槟白是凡尔赛大理石与左岸咖啡馆信纸同一种底色。这组配色试图捕捉法国精神最核心的内在矛盾:极度理性与极度浪漫在同一块土地上共生。',
    philo_en='French colour is never simply colour---it is the material appearance of a worldview. The Republican red holds the guillotine and the rose; the deep blue houses both Descartes\' reason and Monet\'s morning mist; champagne ivory is the same ground tone Versailles marble shares with Left-Bank café paper. The palette tries to catch the central inner contradiction of the French spirit: extreme reason and extreme romance, coexisting on the same patch of land.',
    rows=[
        ((180,32,40), '共和红', 'Marianne Red', 'Rouge Marianne', '180, 32, 40', '三色旗之红,但非正红——波尔多红酒的深度与自由女神帽的激情的中间值', "The Tricolour red, but no flat red---a mid-value between Bordeaux\\'s depth and the passion of the Phrygian cap"),
        ((232,222,205), '香槟象牙', 'Champagne Ivory', 'Ivoire Champagne', '232, 222, 205', '非纯白——香槟气泡的暖调、卢浮宫石灰岩的温度、左岸咖啡馆信纸', 'Not pure white---champagne effervescence, Louvre limestone, and Left-Bank café stationery'),
        ((44,74,138), '共和深蓝', 'Republic Blue', "Bleu R\\'epublique", '44, 74, 138', '三色旗之蓝,取塞夫勒瓷器皇家蓝的深度——启蒙理性的蓝', 'The Tricolour blue, the royal blue of Sèvres porcelain---the blue of Enlightenment reason'),
        ((143,108,148), '普罗旺斯薰衣草', 'Provence Lavender', 'Lavande Proven\\c{c}ale', '143, 108, 148', '南法薰衣草田在午后阳光与灰白石灰土之间呈现的真实颜色', 'The true colour of a Provençal lavender field between afternoon sun and chalk-grey soil'),
        ((142,133,58), '凡尔赛橄榄金', 'Versailles Olive', "Olive Dor\\'ee", '142, 133, 58', '凡尔赛宫正式花园修剪黄杨篱的金绿——古典法式园林美学', 'The gold-green of clipped box hedge in the formal garden of Versailles---the colour of classical French parterre aesthetics'),
        ((122,126,132), '巴黎锌灰', 'Parisian Zinc', 'Zinc Parisien', '122, 126, 132', '奥斯曼改造后巴黎屋顶锌板在阴天的反光色', 'The reflection of Haussmannian Parisian zinc roof under overcast sky'),
    ],
    sub2_zh='法兰西精神的色彩结构', sub2_en='Colour Structure of the French Spirit',
    bullets=[
        ('三色旗的再解读',     '共和红、香槟象牙、共和深蓝并非原版三色旗的复刻,而是对三色精神的去符号化再提炼:红被赋予波尔多的重量,白被赋予时间的温度,蓝被赋予启蒙的深度——旗帜是政治的,这组色是文化的', 'Tricolour Reread: Rouge Marianne, Ivoire Champagne, and Bleu République are not the flag reproduced but its spirit de-symbolised and re-distilled---red is given the weight of Bordeaux, white the temperature of time, blue the depth of the Enlightenment. The flag is political; this palette is cultural'),
        ('南北气质的张力',     '普罗旺斯薰衣草与巴黎锌灰构成法国南北最核心的精神对立:南法是感官、土地、阳光与慵懒的浪漫;巴黎是理性、几何、灰色天空与克制的优雅',                                                'North-South Tension: Lavande Provençale and Zinc Parisien form France\'s deepest spiritual opposition---the south is the sense, soil, sun, and lazy romance; Paris is reason, geometry, grey sky, and restrained elegance'),
        ('先锋撞色的潜伏',     '凡尔赛橄榄金与共和深蓝的并置是全组最具先锋张力的组合:一个属于太阳王的古典秩序,一个属于共和革命的理性锋芒——色相接近却语义对立',                                                  'Avant-Garde Strike Latent: Olive Dorée placed against Bleu République is the most avant-garde pairing in the set---one belongs to the Sun King\'s classical order, the other to the rational edge of republican revolution---hues close, semantics opposed'),
        ('克制高级的实现路径', '六色均经过刻意的饱和度压制:红不燃烧,蓝不冰冷,紫不妖艳,金不张扬,灰不死板,白不刺目。法国人所理解的「高级」,从来不是色彩的强度,而是色彩恰到好处地收敛自身',                  'Restrained Elegance: Every tone is deliberately tamed in saturation---red does not burn, blue does not chill, violet does not flirt, gold does not boast, grey does not deaden, white does not glare. The French sense of "elegance" has never been the intensity of colour, but its trained, exact self-restraint'),
        ('土地温暖的隐线',     '香槟象牙与普罗旺斯薰衣草共同编织这组配色的「土地感」底线:前者是石灰岩与小麦的暖,后者是干燥薰衣草与灰白土壤的暖——法国的浪漫从不悬浮在空中',                                  'Earthbound Warmth: Ivoire Champagne and Lavande Provençale weave the palette\'s "earth-sense" baseline---one the warmth of limestone and wheat, the other the warmth of dried lavender and chalk soil. French romance has never hung in midair'),
    ]
))

# palette 22 — Kyoto (京都)
P.append(dict(
    num=22, name='Kyoto',
    philo_zh='京都的颜色从不主动开口——它们等待被看见。禅院的苔绿不争,枯山水的白砂不语,町家杉木的茶褐在雨中沉默,暗绀的夜空压着千年古都不作声。唯有朱红鸟居,在一切克制之中以极小的面积燃烧最大的温度,像茶室里一枝单花,冷寂里的那一点热烈。',
    philo_en='The colours of Kyoto never speak first---they wait to be seen. The moss green of the Zen courtyard does not compete, the white gravel of the karesansui says nothing, the tea-brown of machiya cedar is silent in the rain, the deep-indigo night sky presses the thousand-year capital without a sound. Only the vermilion torii, amid all this restraint, burns the highest temperature in the smallest area---like a single stem in the tea room, the one point of heat inside the cold and still.',
    rows=[
        ((234,226,212), '绢白', 'Silk White', '\\foreignname{絹白} \\textperiodcentered\\ Kinushiro', '234, 226, 212', '西阵织绢布与和纸漉纸的底色,蚕丝与楮树皮的天然暖调', 'The ground of Nishijin silk and washi paper, the natural warm tone of silkworm and paper-mulberry'),
        ((110,84,64), '枯茶褐', 'Withered Tea', '\\foreignname{枯茶} \\textperiodcentered\\ Karacha', '110, 84, 64', '町家百年杉木柱在时间与炉烟中形成的褐色,千利休「侘び」的颜色', "The brown of a century-old machiya cedar pillar shaped by time and hearth smoke---the colour of Rikyū\\'s wabi"),
        ((204,184,178), '樱灰粉', 'Cherry Grey', '\\foreignname{桜鼠} \\textperiodcentered\\ Sakura-nezumi', '204, 184, 178', '落樱覆于石灯笼上被雨水晕开后的颜色,物哀的精确定义', 'Fallen cherry on a stone lantern, blurred by rain---the precise definition of mono no aware'),
        ((116,126,120), '青竹灰', 'Bamboo Grey', '\\foreignname{青竹鼠} \\textperiodcentered\\ Aotake-nezumi', '116, 126, 120', '岚山竹林晨雾中的竹节色,冷暖平衡的禅理体现', 'The bamboo node in the dawn mist of the Arashiyama grove, a Zen statement of warm-cool balance'),
        ((80,94,68), '苔色', 'Moss Colour', '\\foreignname{苔色} \\textperiodcentered\\ Koke-iro', '80, 94, 68', '龙安寺枯山水石组底部苔藓的深绿,时间留下的暗哑印记', 'The deep moss green at the foot of the Ryōan-ji stones, the dull print time has left'),
        ((34,40,66), '紺', 'Deep Indigo', '\\foreignname{紺} \\textperiodcentered\\ Kon', '34, 40, 66', '能剧服装与京友禅夜色图案的深靛蓝,冥想状态本身的颜色', 'The deep indigo of Noh costume and Kyoto-Yuzen night patterns---the colour of meditation itself'),
    ],
    sub2_zh='京都精神的色彩结构', sub2_en='Colour Structure of the Kyoto Spirit',
    bullets=[
        ('留白为骨',           '绢白与樱灰粉共同构建配色的呼吸空间,前者是空无、负形、茶室墙面,后者是将消未消的感知边界——京都美学不在于填满,而在于知道哪里应当什么都没有',                                  'Negative Space as Bone: Kinushiro and Sakura-nezumi build the palette\'s breathing room---the former is void, negative form, the tea-room wall; the latter is the perceptual edge of fading-not-yet-gone. Kyoto aesthetics is not about filling in, but about knowing where there should be nothing'),
        ('冷暖天平',           '六色底中,枯茶褐与苔绿属暖调,暗绀与青竹灰属冷调,樱灰粉与绢白居中游移——四季平衡,禅院冷寉与町家温暖在此精确对位',                                                                'Warm/Cool Balance: Among the six grounds, Karacha and Koke-iro are warm, Kon and Aotake-nezumi are cool, Sakura-nezumi and Kinushiro drift in between---four-season balance, the cold stillness of the Zen courtyard exactly counterpointed with the warmth of machiya'),
        ('幽玄的低饱和逻辑',   '所有色彩均经过刻意的去鲜亮处理,模拟京都特有的盆地晨雾对色彩的柔化效果——雾不消色,只让色彩向内收,这正是「幽玄」的物理机制',                                                    'Yūgen via Low Saturation: All colours are deliberately stripped of brightness, mimicking Kyoto\'s basin morning mist---the mist does not erase colour but draws it inward, which is the very physics of yūgen'),
        ('水墨留白的东方结构', '整组配色可理解为一幅水墨:暗绀是浓墨,苔绿是中墨,枯茶褐是淡墨,青竹灰是宿墨,樱灰粉是墨的晕散,绢白是纸——朱红是画师最后蘸朱砂落下的那一点钤印',                              'Ink-Wash Eastern Structure: The whole palette can be read as one ink-wash---Kon is the deep ink, Koke-iro the middle ink, Karacha the light ink, Aotake-nezumi the spent ink, Sakura-nezumi the ink\'s diffusion, Kinushiro the paper---and an unseen vermilion is the painter\'s final cinnabar seal'),
    ]
))


# palette 23 — Siamese Dream
P.append(dict(
    num=23, name='Siamese Dream',
    philo_zh='《Siamese Dream》的封面本身就是一张配色宣言——两个女孩在柔焦的暖白光晕里相依,背景的深绿若隐若现,橙黄的光线像记忆里某个下午,美好得不真实。这不是摇滚专辑封面惯用的高对比冲击美学,而是一种刻意制造的梦境质感:过曝、柔化、带着胶片颗粒的温柔失真——如同 Corgan 把最原始的情感录进了最失真的吉他音墙里。',
    philo_en='The cover of \\emph{Siamese Dream} is itself a palette manifesto---two girls leaning into each other inside a softly out-of-focus warm halo, a faint deep green pressing in from behind, an orange light spilling through like some afternoon out of memory, beautiful past the point of belief. This is not the high-contrast assault that rock-album sleeves usually reach for; it is a deliberately constructed dream texture---overexposed, soft, tender film-grain distortion---just as Corgan poured the rawest emotion into the most distorted wall of guitars.',
    rows=[
        ((238,226,208), '终章暖白', 'Luna',      'Luna',      '238, 226, 208', '封面的暖白光晕,专辑最后一首歌的余韵——不是纯白,是胶片过曝后仍保留的一丝人间温度,是梦醒前最后的柔光',                          'The warm white halo of the cover, the lingering breath of the album\'s closing track---not pure white, but the trace of human warmth that survives film overexposure, the last soft light before waking'),
        ((182,180,193), '裸露灰紫', 'Disarm',    'Disarm',    '182, 180, 193', '洗白的灰紫,Disarm 是整张专辑里防御最低的时刻,弦乐与铃声剥去了所有失真——这是玻璃碎裂前的颜色,透明、脆、带着童年创伤的寒意', 'A washed-out grey-violet. \\emph{Disarm} is the album\'s least-defended moment, strings and bells stripping every layer of distortion---the colour just before glass shatters: transparent, brittle, carrying the chill of childhood wounds'),
        ((198,158,65),  '可疑旧金', 'Today',     'Today',     '198, 158, 65',  '沾了尘的旧金色,Today 听起来是全碟最明媚的旋律,却是 Corgan 最黑暗时刻的产物——这抹金因此必须是褪色的、带着微苦的甜,美丽而不可信任',  'A dusted, antiqued gold. \\emph{Today} sounds like the brightest melody on the record yet was born of Corgan\'s darkest days---so this gold must be faded, slightly bitter beneath its sweetness, beautiful and not to be trusted'),
        ((150,145,135), '悬浮烟灰', 'Hummer',    'Hummer',    '150, 145, 135', '烟灰褐,Hummer 用层层叠叠的音墙制造一种失重的悬浮感——这是梦游者眼中的颜色,既不清醒也不沉睡,是 shoegaze 美学最诚实的物质形态',    'Smoke-ash brown. \\emph{Hummer} stacks wall after wall of guitar to manufacture a weightless suspension---this is the colour seen by a sleepwalker, neither awake nor asleep, the most honest material form of shoegaze aesthetics'),
        ((188,105,40),  '低温烧橙', 'Mayonaise', 'Mayonaise', '188, 105, 40',  '深而沉的烧橙,封面光源的颜色——Mayonaise 是全碟最慢、最痛、最私密的曲目,这抹橙不是热情而是积压已久的情感在低温中缓慢焦化的颜色',  'A deep, settled burnt orange, the colour of the cover\'s light source. \\emph{Mayonaise} is the slowest, most painful, most private cut on the record---this orange is not warmth but the slow, low-temperature caramelisation of an emotion held in too long'),
        ((42,68,48),    '深渊暗绿', 'Soma',      'Soma',      '42, 68, 48',    '封面背景若隐若现的深绿,九分钟的史诗长曲从轻柔攀爬至崩塌——这是有机物在黑暗中生长的颜色,苔藓与腐叶,美丽与窒息共生',          'The deep green half-hidden behind the cover, the nine-minute epic that climbs from tender hush to collapse---the colour of organic matter growing in darkness, moss and rotting leaves, where beauty and suffocation share the same body'),
    ],
    sub2_zh='青春期情感的悖论结构', sub2_en='The Paradox Structure of Adolescent Feeling',
    bullets=[
        ('梦境包裹与失真美学',        'Luna 的暖白与 Hummer 的烟灰共同构成专辑的“失焦层”——一切痛苦都先被过曝、被柔化、被音墙包住,然后才允许被听见。这不是回避痛苦,而是让痛苦以可承受的密度释放',                                                'Dream-Wrap and Distortion: Luna\'s warm white and Hummer\'s smoke-ash together form the record\'s \\emph{out-of-focus layer}---every pain is first overexposed, softened, and wrapped in a wall of sound before it is allowed to be heard. Not avoidance, but releasing pain at a survivable density'),
        ('美丽容器装最重的内容',       'Today 的旧金与 Disarm 的灰紫是悖论的两极:前者用明媚旋律包裹自毁倾向,后者用童谣式的铃声讲述童年创伤——Corgan 始终用最美的容器装最重的内容,这是 Siamese Dream 最核心的情感策略',                                'Beautiful Vessels for the Heaviest Contents: Today\'s tarnished gold and Disarm\'s grey-violet sit at opposite poles of the paradox---the former dresses self-destructive impulse in a bright melody, the latter tells a childhood wound through music-box bells. Corgan always pours the heaviest contents into the most beautiful vessel; this is the album\'s core emotional strategy'),
        ('情感核心的低温焦化',         'Mayonaise 的烧橙是整组配色的情感核心(pal5=primary 也正落在此处)——不是燃烧的红,而是已经燃烧过、被时间慢烤、被自身重量压低的橙。它告诉读者:这里的热度不来自爆发,而来自长期不灭',                                  'Low-Temperature Caramelisation at the Emotional Core: Mayonaise\'s burnt orange is the palette\'s emotional core (and conveniently the pal5=primary slot)---not red on fire, but orange that has already burned, slow-roasted by time, weighted down by its own gravity. The heat here is not from explosion but from refusing to go out'),
        ('深渊作为最深锚点',           'Soma 的暗绿(pal6=accent)是六色中唯一的“黑色替身”——它不是纯黑,而是有机物的黑,是苔藓、腐叶、深林。整组配色因此从不依赖纯黑来收尾,而是用一种“仍在生长的黑暗”把整张专辑稳稳压住',                            'The Abyss as Deepest Anchor: Soma\'s deep green (pal6=accent) is the only \\emph{black-substitute} among the six---not pure black but organic black, the black of moss, leaf-rot, and deep forest. The palette never anchors on pure black; it presses the record down with a darkness that is still alive and still growing'),
        ('回避高饱和与强对比的渗透美学', '六色全部退避鲜亮,因为 Siamese Dream 的情绪从不“爆炸”——它“渗透”。没有任何一色试图夺取注意力,反而每一色都在以最低的姿态长时间地停留在视觉里,如同 shoegaze 的吉他延音',                              'Permeation over Saturation: All six colours retreat from brightness because \\emph{Siamese Dream}\'s feelings never explode---they seep. No single colour fights for attention; each lingers at its lowest posture, the way a shoegaze guitar sustains long after the strike'),
    ]
))


# ---------------------------------------------------------------------------
# Rendering

ZH_HEADER_ROW = r'''\toprule\rowcolor{booktableheadcolor}
\booktableheadcell{} & \booktableheadcell{中文名} & \booktableheadcell{原名} & \booktableheadcell{RGB} & \booktableheadcell{释义} \\
\midrule'''

EN_HEADER_ROW = r'''\toprule\rowcolor{booktableheadcolor}
\booktableheadcell{} & \booktableheadcell{Name} & \booktableheadcell{Original} & \booktableheadcell{RGB} & \booktableheadcell{Gloss} \\
\midrule'''


def render_table(p, lang):
    out = []
    out.append(r'\begin{fullwidth}\small\noindent')
    out.append(r'\begin{tabularx}{\linewidth}{@{}clllX@{}}')
    out.append(ZH_HEADER_ROW if lang == 'zh' else EN_HEADER_ROW)
    for rgb, name_zh, name_en, name_orig, rgb_str, gloss_zh, gloss_en in p['rows']:
        swatch = f"\\bookcardswatch{{{rgb[0]},{rgb[1]},{rgb[2]}}}"
        if lang == 'zh':
            # ZH template: Name = Chinese; Original = native-language form
            out.append(f"{swatch} & {name_zh} & {name_orig} & {rgb_str} & {gloss_zh} \\\\")
        else:
            # EN template: Name = English; Original = native-language form
            out.append(f"{swatch} & {name_en} & {name_orig} & {rgb_str} & {gloss_en} \\\\")
    out.append(r'\bottomrule')
    out.append(r'\end{tabularx}\end{fullwidth}')
    return '\n'.join(out)


def render_bullets(p, lang):
    out = [r'\begin{palettebullets}']
    for name, desc_zh, desc_en in p['bullets']:
        if lang == 'zh':
            out.append(f"\\item \\textbf{{{name}}} --- {desc_zh}")
        else:
            # For palettes where the bullet "name" is Chinese (structural-logic style),
            # the English descriptor starts with "English Label: real description".
            # Extract that English label and use it instead of the Chinese name.
            m = re.match(r'^([^:]+):\s+(.*)$', desc_en)
            if any('\u4e00' <= c <= '\u9fff' for c in name) and m:
                label, body = m.group(1), m.group(2)
                out.append(f"\\item \\textbf{{{label}}} --- {body}")
            else:
                out.append(f"\\item \\textbf{{{name}}} --- {desc_en}")
    out.append(r'\end{palettebullets}')
    return '\n'.join(out)


# Map of macron / overline chars to TeX accent commands.
_ACCENT_MAP = {
    'ā': r'\=a', 'ē': r'\=e', 'ī': r'\=i', 'ō': r'\=o', 'ū': r'\=u',
    'Ā': r'\=A', 'Ē': r'\=E', 'Ī': r'\=I', 'Ō': r'\=O', 'Ū': r'\=U',
    'ȳ': r'\=y', 'Ȳ': r'\=Y',
}

_CYRILLIC_RE = re.compile(r'[\u0400-\u04FF]+(?:[\s\-\u2014][\u0400-\u04FF]+)*')


def post_process_en(text):
    # Wrap contiguous Cyrillic runs with \foreignname{...}, but skip those already wrapped.
    def repl(m):
        s = m.group(0)
        # Find the position; check if already inside a \foreignname{...}
        start = m.start()
        # Look backwards for '\foreignname{' without a closing '}' in between.
        seg = text[:start]
        depth_open = seg.count(r'\foreignname{')
        # Count closing braces after the last \foreignname{
        last = seg.rfind(r'\foreignname{')
        if last != -1:
            after = seg[last + len(r'\foreignname{'):]
            depth = 1
            for ch in after:
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
                if depth == 0:
                    break
            if depth > 0:
                return s  # already inside a \foreignname{}
        return f"\\foreignname{{{s}}}"
    text = _CYRILLIC_RE.sub(repl, text)
    # Replace macron characters with TeX accent macros.
    for ch, repl_str in _ACCENT_MAP.items():
        text = text.replace(ch, repl_str + '{}')
    return text


def render_card(p, lang):
    title = f"{p['num']}\\enspace {p['name']}"
    philo = p['philo_zh'] if lang == 'zh' else p['philo_en']
    sub1 = '色彩哲学' if lang == 'zh' else 'Colour Philosophy'
    sub2 = p['sub2_zh'] if lang == 'zh' else p['sub2_en']
    parts = [
        f"\\bookpalettecardhead{{{title}}}",
        f"\\palettesubsec{{{sub1}}}",
        f"\\noindent {philo}",
        '',
        render_table(p, lang),
        '',
        f"\\palettesubsec{{{sub2}}}",
        render_bullets(p, lang),
    ]
    return '\n'.join(parts)


def render_file(lang):
    is_zh = (lang == 'zh')
    out = []
    if is_zh:
        out.append('% Palette Introduction --- Chinese.')
    else:
        out.append('% Palette Introduction --- English.')
    out.append('% Auto-generated by gen_palette_intro.py.  Do not edit by hand.')
    if is_zh:
        out.append(r'\chapter{调色板介绍}\label{ch:palette-intro}')
        out.append('')
        out.append('本章按编号依次介绍 24 组主题调色板。每一组都保留三段固定结构——\\emph{色彩哲学}阐明配色背后的世界观,\\emph{六色配色组}列出 \\texttt{pal1} 到 \\texttt{pal6} 的色值与释义,随后的小节(\\emph{设计思路}、\\emph{色彩结构}或\\emph{美学法则}等)再对每一色或每一条结构性原则展开说明。配色按编号顺序排列、自然分页,不再强制每页限定数量,只保证六色配色表保持完整、不被分割。')
    else:
        out.append(r'\chapter{Palette Introduction}\label{ch:palette-intro}')
        out.append('')
        out.append('This chapter walks through all twenty-four themed palettes in order. Every entry keeps a fixed three-part structure---a \\emph{Colour Philosophy} stating the worldview behind the palette, a \\emph{six-colour table} listing the values and gloss of \\texttt{pal1} through \\texttt{pal6}, and a closing subsection (\\emph{Design Notes}, \\emph{Colour Structure}, or \\emph{Aesthetic Rules} as appropriate) unfolding either per-colour annotations or structural principles. Palettes are laid out sequentially with natural page breaks; the only constraint enforced is that each six-colour table is kept intact on a single page.')
    out.append('')
    # All 24 palettes laid out sequentially.  Separator is just \par\bigskip so
    # pages fill naturally; tabularx tables are atomic and never split.
    for i in range(len(P)):
        out.append('% ---------------------------------------------------------------------------')
        out.append(render_card(P[i], lang))
        if i < len(P) - 1:
            out.append(r'\par\bigskip')
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    with open('chapter-zh/palette-intro-zh.tex', 'w', encoding='utf-8') as f:
        f.write(post_process_en(render_file('zh')).replace('→', r'$\to$'))
    with open('chapter-en/palette-intro-en.tex', 'w', encoding='utf-8') as f:
        f.write(post_process_en(render_file('en')).replace('→', r'$\to$'))
    print(f"wrote {len(P)} palettes")
