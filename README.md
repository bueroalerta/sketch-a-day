----
# sketch-a-day
### one visual idea a day [[on GitHub!](https://github.com/villares/sketch-a-day)]

Hi! I'm [Alexandre Villares](https://abav.lugaralgum.com), let's see if I can make one small program (*sketch*) a day. I'm working mostly with [Processing Python Mode](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN) and sometimes [Processing Java Mode](https://processing.org) and[P5JS (JavaScript)](p5js.org) or other stuff.

If you enjoy this, make a small donation [here](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=HCGAKACDMVNV2) or with [Patreon](https://patreon.com/arteprog)

----

![s096](s096/s096.gif)

096: [code](https://github.com/villares/sketch-a-day/tree/master/s096)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

More 'Inputs' helper changes (WASD & arrows for sliders). New GIF export helper actually works now!
More lone nodes and edge creation changes...

----

![s095](s095/s095.gif)

095: [code](https://github.com/villares/sketch-a-day/tree/master/s095)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Complete rewrite of the 'Inputs' helper

```
# Ask user for Arduino port, uses slider if none is selected, use on `setup()`
global input
input = Input(Arduino)

# on `draw()`read analog pins 1, 2, 3, 4 or sliders
pot1 = input.analog(1)
pot2 = input.analog(2)
pot3 = input.analog(3)
pot4 = input.analog(4)

tilt = input.digital(13) # also triggered by [space bar]

# When on sliders, this draws them and checks mouse dragging / keystrokes
input.update()

```

----

![s094](s094/s094.gif)

094: [code](https://github.com/villares/sketch-a-day/tree/master/s094)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Connection 'rate' can be less than 1, prevents less than 2 nodes

----

![s093](s093/s093.gif)

093: [code](https://github.com/villares/sketch-a-day/tree/master/s093)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Nodes without connection are now removed

```
    COM_ARESTAS = set()  # para guardar pontos com aresta
    for aresta in Aresta.ARESTAS:
        if (aresta.p1 not in Ponto.SET) or (aresta.p2 not in Ponto.SET)\
                or (aresta.p1 is aresta.p2):  # arestas degeneradas
            Aresta.ARESTAS.remove(aresta)   # remove a aresta
        else:                # senão, tudo OK!
            aresta.desenha()  # desenha a linha
            aresta.puxa_empurra(TAM_ARESTA)  # altera a velocidade dos pontos
            # Adiciona ao conjunto de pontos com aresta
            COM_ARESTAS.update([aresta.p1, aresta.p2])
    Ponto.SET = COM_ARESTAS  # isto remove pontos sem nenhuma aresta
 
```



----

![s092](s092/s092.gif)

092: [code](https://github.com/villares/sketch-a-day/tree/master/s092)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Dynamic change of connection rate

```
if NUM_PONTOS * NUM_CONNECT > len(Aresta.ARESTAS):
        rnd_choice(list(Ponto.SET)).cria_arestas()
    elif NUM_PONTOS * NUM_CONNECT < len(Aresta.ARESTAS):
        Aresta.ARESTAS.remove(rnd_choice(Aresta.ARESTAS))
```

----

![s091](s091/s091.gif)

091: [code](https://github.com/villares/sketch-a-day/tree/master/s091)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Major rethink of my Arduino/Firmata code. I can now choose on start between sliders and potentiometers.

----

![s090](s090/s090.gif)

090: [code](https://github.com/villares/sketch-a-day/tree/master/s090)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Opaque strokes, no fill, randomized colours by column.

----

![s089](s089/s089.gif)

089: [code](https://github.com/villares/sketch-a-day/tree/master/s089)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

X stroke now is translucent and grid elements have random colour inside grids.

----

![s088](s088/s088.gif)

088: [code](https://github.com/villares/sketch-a-day/tree/master/s088)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Filled rects, ellipses and losangles (without sktroke) and Xs

----

![s087](s087/s087.gif)

087: [code](https://github.com/villares/sketch-a-day/tree/master/s087)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

No fill again, less colours. Variable/random number of elements per grid.

----

![s086](s086/s086.gif)

086: [code](https://github.com/villares/sketch-a-day/tree/master/s086)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Translucent fill & some stroke weight

----

![s085](s085/s085.gif)

085: [code](https://github.com/villares/sketch-a-day/tree/master/s085)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Some colour, and some crazy meddling with the Slider class...

----

![s084](s084/s084.gif)

084: [code](https://github.com/villares/sketch-a-day/tree/master/s084)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Make the grid's position/origin align based on the spacing size (super- grid)

----

![s083](s083/s083.gif)

083: [code](https://github.com/villares/sketch-a-day/tree/master/s083)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Xs and rotated rectangles

----

![s082](s082/s082.gif)

082: [code](https://github.com/villares/sketch-a-day/tree/master/s082)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Squares and ellipses

----

![s081](s081/s081.gif)

081: [code](https://github.com/villares/sketch-a-day/tree/master/s081)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Let's try some grids

----

![s080](s080/s080.gif)

080: [code](https://github.com/villares/sketch-a-day/tree/master/s080)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

More arrows (black and white alternate by generation)

----

![s079](s079/s079.gif)

079: [code](https://github.com/villares/sketch-a-day/tree/master/s079)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Arrows (right black, left white)

----

![s078](s078/s078.gif)

078: [code](https://github.com/villares/sketch-a-day/tree/master/s078)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Color

----

![s077](s077/s077.gif)

077: [code](https://github.com/villares/sketch-a-day/tree/master/s077)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Random branch reduction is now less simmetric, and random seed changes on depth change.

----

![s076](s076/s076.gif)

076: [code](https://github.com/villares/sketch-a-day/tree/master/s076)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Stroke weight and some transparency

----

![s075](s075/s075.gif)

075: [code](https://github.com/villares/sketch-a-day/tree/master/s075)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

... and slightly different parameters and recursion level control instead of lenght

----

![s074](s074/s074.gif)

074: [code](https://github.com/villares/sketch-a-day/tree/master/s074)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Adaptomg Shiffmans recusive Tree, with sliders or Pots...

----

![s073](s073/s073.gif)

073: [code](https://github.com/villares/sketch-a-day/tree/master/s073)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

The code remains ugly :(

----

![s072](s072/s072.gif)

072: [code](https://github.com/villares/sketch-a-day/tree/master/s072)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Let's mix some arrows?

----

![s071](s071/s071.gif)

071: [code](https://github.com/villares/sketch-a-day/tree/master/s071)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Thicker and with a saturation slider (no more scale offset)

----

![s070](s070/s070.gif)

070: [code](https://github.com/villares/sketch-a-day/tree/master/s070)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Thicker and with a saturation slider (no more scale offset)

----

![s069](s069/s069.gif)

069: [code](https://github.com/villares/sketch-a-day/tree/master/s069)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Added rotation.

----

![s068](s068/s068.gif)

068: [code](https://github.com/villares/sketch-a-day/tree/master/s068)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

... and with sliders (by [Peter Farell](https://github.com/hackingmath/python-sliders))

----

![s067](s067/s067.gif)

067: [code](https://github.com/villares/sketch-a-day/tree/master/s067)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Something else.

----

![s066](s066/s066.gif)

066: [code](https://github.com/villares/sketch-a-day/tree/master/s066)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Arrow grid networks can be sized and placed...

----

![s065](s065/s065.gif)

065: [code](https://github.com/villares/sketch-a-day/tree/master/s065)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Arrow grid networks are now objects...

----

![s064](s064/s064.gif)

064: [code](https://github.com/villares/sketch-a-day/tree/master/s064)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Revisiting yet an older graph, adding arrows...

----

![s063](s063/s063.gif)

063: [code](https://github.com/villares/sketch-a-day/tree/master/s063)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Revisiting an older graph adding arrows...

----

![s062](s062/s062.gif)

062: [code](https://github.com/villares/sketch-a-day/tree/master/s062)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

`+` and `-` keys control the distange/range of targes in 0.5 * SPACING increments

----

![s061](s061/s061.gif)

061: [code](https://github.com/villares/sketch-a-day/tree/master/s061)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Sometimes we have multiple arrows now out of each node...But I reduced the range (distance) they can point to.

----

![s060](s060/s060.gif)

060: [code](https://github.com/villares/sketch-a-day/tree/master/s060)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Complete Object Oriented refactor...

----

![s059](s059/s059.gif)

059: [code](https://github.com/villares/sketch-a-day/tree/master/s059)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Back to a list of points, now every point of the grid has a node. Limited points_to random each.

----

![s058](s058/s058.gif)

058: [code](https://github.com/villares/sketch-a-day/tree/master/s058)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Now with some deepcopy of changeable imutable namedtuples (containing mutable lists), and some lerp()

----

![s057](s057/s057.gif)

057: [code](https://github.com/villares/sketch-a-day/tree/master/s057)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Revisited 54 and now I'm re-selecting random points_to nodes...

----

![s056](s056/s056.gif)

056: [code](https://github.com/villares/sketch-a-day/tree/master/s056)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Arrow grid moving in HSB colour space

----

![s055](s055/s055.png)

055: [code](https://github.com/villares/sketch-a-day/tree/master/s055)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Grid revisited

----

![s054](s054/s054.gif)

054: [code](https://github.com/villares/sketch-a-day/tree/master/s054)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

New arrows! With a "Tail" parameter...

----

![s053](s053/s053.png)

053: [code](https://github.com/villares/sketch-a-day/tree/master/s053)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Big invisible refactor (no more point-grid to select from, now a list of possible X and Y positons to choose).
On the visible side, fewer elements, and non-pointing elements redrawn in red on top.

----

![s052](s052/s052.png)

052: [code](https://github.com/villares/sketch-a-day/tree/master/s052)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

White lines first, black arrows on top.

----

![s051](s051/s051.gif)

051: [code](https://github.com/villares/sketch-a-day/tree/master/s051)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Points  now on a grid.

----

![s050](s050/s050.gif)

050: [code](https://github.com/villares/sketch-a-day/tree/master/s050)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

Arrows now...

----

![s049](s049/s049.gif)

049: [code](https://github.com/villares/sketch-a-day/tree/master/s049)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Yet more graphs

----

![s048](s048/s048.gif)

048: [code](https://github.com/villares/sketch-a-day/tree/master/s048)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Yet more graphs

----

![s047](s047/s047.gif)

047: [code](https://github.com/villares/sketch-a-day/tree/master/s047)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Yet more graphs

----

![s046](s046/s046.png)

046: [code](https://github.com/villares/sketch-a-day/tree/master/s046)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Yet more graphs

----

![s045](s045/s045.gif)

045: [code](https://github.com/villares/sketch-a-day/tree/master/s045)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Yet more graphs

----

![s044](s044/s044.gif)

044: [code](https://github.com/villares/sketch-a-day/tree/master/s044)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
More graphs

----

![s043](s043/s043.png)

043: [code](https://github.com/villares/sketch-a-day/tree/master/s043)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
More graphs

----

![s042](s042/s042.gif)

042: [code](https://github.com/villares/sketch-a-day/tree/master/s042)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Yet another interactive recursive thingy, the image on the right is shown with a key pressed

----

![s041](s041/s041.png)


041: [code](https://github.com/villares/sketch-a-day/tree/master/s041)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Yet another interactive recursive thingy, the image on the right is shown with a key pressed

----

![040](sketch_180209a/sketch_180209a.png)
![040](sketch_180209a/sketch_180209a_2.png)

040: [sketch_180209a](https://github.com/villares/sketch-a-day/tree/master/sketch_180209a)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
More recursion

----

![039](sketch_180208e/sketch_180208e.png)

039: [sketch_180208e](https://github.com/villares/sketch-a-day/tree/master/sketch_180208e)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Manoloide  inspired recursion

----

![038](sketch_180208d/sketch_180208d.png)

038: [sketch_180208d](https://github.com/villares/sketch-a-day/tree/master/sketch_180208d)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Saskia Freeke inspired grid

----

![037](sketch_180206a/sketch_180206a.gif)

037: [sketch_180206b](https://github.com/villares/sketch-a-day/tree/master/sketch_180206a)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
"Carnahacking is near!"

----

![036](sketch_180205b/sketch_180205b.png)

036: [sketch_180205b](https://github.com/villares/sketch-a-day/tree/master/sketch_180205b)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Added some mouse disturbance

----

![035](sketch_180204b/sketch_180204b.gif)

035: [sketch_180204b](https://github.com/villares/sketch-a-day/tree/master/sketch_180204b)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Preparing for "Carnahacking"

----

![034](sketch_180203c/sketch_180203c.gif)

034: [sketch_180203c](https://github.com/villares/sketch-a-day/tree/master/sketch_180203c)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Like 33 but again with "w squared" circles

----

![033](sketch_180202c/sketch_180202c.png)

033: [sketch_180202c](https://github.com/villares/sketch-a-day/tree/master/sketch_180202c)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Like 32 but again with lines

----

![032](sketch_180201c/sketch_180201c.gif)

032: [sketch_180201c](https://github.com/villares/sketch-a-day/tree/master/sketch_180201c)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Like 29 but with moving points after the gesture is done

----


![031](sketch_180131c/sketch_180131c.gif)

031: [sketch_180130c](https://github.com/villares/sketch-a-day/tree/master/sketch_180131c)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Like 29 but with moving points after the gesture is done

----

![030](sketch_180130c/sketch_180130c.png)

030: [sketch_180130c](https://github.com/villares/sketch-a-day/tree/master/sketch_180130c)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Like 29 but with 3D and PeasyCam orbit...

----

![29c](sketch_180129c/sketch_180129c.gif)

029: [sketch_180129c](https://github.com/villares/sketch-a-day/tree/master/sketch_180129c)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Like 27 but with circles

----

![28c](sketch_180128c/sketch_180128c.png)

028: [sketch_180128c](https://github.com/villares/sketch-a-day/tree/master/sketch_180128c)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Like 27 but on grayscale

----

![27c](sketch_180127c/sketch_180127c.png)

027: [sketch_180127c](https://github.com/villares/sketch-a-day/tree/master/sketch_180127c)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)][YouTube](https://www.youtube.com/watch?v=A-rqkru79Dw)

Saving a list of points to animate colour... Mouse speed changes recorded colour &  strokeWeight()

----

![26](sketch_180126c/sketch_180126c.png)

026: [sketch_180126c](https://github.com/villares/sketch-a-day/tree/master/sketch_180126c)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Mouse speed changing colour &  strokeWeight()

----

![25](sketch_180125c/sketch_180125c.png)

025c: [sketch_180125b](https://github.com/villares/sketch-a-day/tree/master/sketch_180125c)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Mouse speed changing strokeWeight()

----

![24](sketch_180124b/sketch_180124b.png)

024b: [sketch_180124b](https://github.com/villares/sketch-a-day/tree/master/sketch_180124b)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]  Maybe tomorrow I'll try adding some sliders & movement to this graph ? [nah...]

----

![23](sketch_180123b/sketch_180123b.gif)

023b: [sketch_180123b](https://github.com/villares/sketch-a-day/tree/master/sketch_180123b)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]  Farrel's Sliders adding random displacement

----

022: missed :(

----

![21b](sketch_180121b/sketch_180121b.gif)

021b: [sketch_180121b](https://github.com/villares/sketch-a-day/tree/master/sketch_180121b)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Playing with Peter "[Hacking Math Class](http://twitter.com/hackingmath)" Farrel's Sliders!

----

![20b](sketch_180120b/sketch_180120b.gif)

020b: [sketch_180120b](https://github.com/villares/sketch-a-day/tree/master/sketch_180120b)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
I was stuck on my DBN conversion sketch 20a, so this HSB shape play is 20b...

![20a](sketch_180120a/sketch_180120a.png)

020a: [sketch_180120a](https://github.com/villares/sketch-a-day/tree/master/sketch_180120a)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
Refactored the code generation, removed most of the repeated vertices... C D E G O R not nice yet…

----

![19a](sketch_180119a/sketch_180119a.png)

019: [sketch_180119a](https://github.com/villares/sketch-a-day/tree/master/sketch_180119a)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] DBN Letters: Now working on a new approach, generating vertex/Shape code, not there yet...

----

![18a](sketch_180118a/sketch_180118a.png)

018: [sketch_180118a](https://github.com/villares/sketch-a-day/tree/master/sketch_180118a)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] DBN Color font? Nah…

----

![17a](sketch_180117a/sketch_180117a.png)

017: [sketch_180117a](https://github.com/villares/sketch-a-day/tree/master/sketch_180117a)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] John Maeda's `dbnletters.dbn` code from Design by Numbers on Processing Python Mode

----

![16a](sketch_180116a/sketch_180116a.png)

016: [16a](https://github.com/villares/sketch-a-day/tree/master/sketch_180116a)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] Converting some Typography code from Design by Numbers, almost there!

----

![15a](sketch_180115a/sketch_180115a.png)

015: [sketch_180115a](https://github.com/villares/sketch-a-day/tree/master/sketch_180115a)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] Converting some Typography code from Design by Numbers, first trials

----

![14a](sketch_180114a/sketch_180114a.png)

014: [sketch_180114a](https://github.com/villares/sketch-a-day/tree/master/sketch_180114a)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] Another 3D Graph

----

![13a](sketch_180113a/sketch_180113a.png)

013: [s180113](https://github.com/villares/sketch-a-day/tree/master/sketch_180113a)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] 3D Graph

----

![s180112](s180112/s180112.png)

012: [s180112](https://github.com/villares/sketch-a-day/tree/master/s180112)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] Another Graph Take

----

![s180111](s180111/s180111.png)

011: [s180111](https://github.com/villares/sketch-a-day/tree/master/s180111)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] A Graph Take

----

![s180110](s180110/s180110.png)

010: [s180110](https://github.com/villares/sketch-a-day/tree/master/s180110)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]  More Manoloide inspired balls [PNG](s180110/s180110.png) (derived from a [sketch](https://gist.github.com/manoloide/16ea9e1d68c6ba1700fcb008fd38aab0) by [Manuel Gamboa Naon](http://manoloide.com))

----

![GIF](s180109/s180109.gif)

009: [s180109](https://github.com/villares/sketch-a-day/tree/master/s180109)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]  Balls for Manoloide  [GIF](s180109/s180109.gif) (derived from a [sketch](https://gist.github.com/manoloide/16ea9e1d68c6ba1700fcb008fd38aab0) by [Manuel Gamboa Naon](http://manoloide.com))

----

![GIF](s180108/s180108.gif)

008: [s180108](https://github.com/villares/sketch-a-day/tree/master/s180108)  [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]   Grid of Platonic Solids in Python Mode [GIF](s180108/s180108.gif)

----

![GIF](s180107/s180107.gif)

007: [s180107](https://github.com/villares/sketch-a-day/tree/master/s180107) [[Processing Java](https://www.processing.org)]  Another grid of Platonic Solids in Java Mode [GIF](s180107/s180107.gif)

----

![GIF](s180106/s180106.gif)

006: [s180106](https://github.com/villares/sketch-a-day/tree/master/s180106) [[Processing Java](https://www.processing.org)]  Grid of Platonic Solids in Java Mode  [GIF](s180106/s180106.gif)

----

005: [s180105](https://github.com/villares/sketch-a-day/tree/master/s180105) [[p5js](https://www.p5js.org)] Line Tetrahedrons in p5*js - [interactive](https://villares.github.io/sketch-a-day/s180105/s180105)

----

![GIF](s180104/s180104.gif)

004: [s180104](https://github.com/villares/sketch-a-day/tree/master/s180104) [[Processing Java](https://www.processing.org)] Tetrahedrons in Java Mode- [GIF](https://github.com/villares/sketch-a-day/tree/master/s180104/s180104.gif)

----

![GIF](s180103/s180103.gif)

003: [s180103](https://github.com/villares/sketch-a-day/tree/master/s180103) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] Tetrahedrons  Python Mode- [GIF](https://github.com/villares/sketch-a-day/tree/master/s180103/s180103.gif)

----

002: [s180102](https://github.com/villares/sketch-a-day/tree/master/s180102) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] Many Stars 3D - [YouTube](https://www.youtube.com/watch?v=QmsthW60iBY)

----

001: [s180101](https://github.com/villares/sketch-a-day/tree/master/s180101)[[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)] Many Stars - [YouTube](https://www.youtube.com/watch?v=gKWBfghDV_w) (inspired by my own [p5js Xmas & New Year card code](https://github.com/villares/p5js-play/tree/master/newYearStars))
