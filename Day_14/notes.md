## Ragav Notes 

## Display

### Block

Block elements occupy entire width of container

- p
- h1-h6
- div
- list

### Inline

Inline elements occupy with of content

- a
- span
- inline

## SVG

Scalar Vector Graphics

- Doesn't get pixelated
- Color them easily
- Smaller size

### Drawback

- No gradients

## 3 ways of CSS

- Inline - ❌
- Internal
  - Reducing the round-trip
  - Cannot be used if the file very long
  - Small size -> Speed up -> Render Tree | Performance
- External - ✅ - 95%
  - Reuse ⬆️ - Add CSS to multiple HTML
  - Separation of concern - HTML & CSS

## Inline

- Donot respect height or width
- Side by Side

## Block

- Respects height and width
- Stacked

## Inline-Block

- Respects height and width
- Side by Side (Enough)
- Stacked (Not enough space)

## Flex

- Apply on the parent element
- Always side by side
- Tries to keep Height constant
- width is just a suggestion


## Extra Notes

### When do we prefer Internal CSS?

- HTML -> converted into DOM Tree
- CSS -> converted into CCSOM Tree
- DOM Tree + CSSOM Tree = Render Tree

If the two doesn't combine -> no render tree -> website looks Blank ❌

index.html will be loaded -> HTML file -> External CSS (2 trips: one for HTML, and one for CSS file)
Until these two trips are complete: Screen is Blank
If External CSS is very heavy, it will take a long time to display something on the screen.
Bottleneck?
Usually the roundtrip

If you could make one trip (combine HTML and CSS) -> it will be faster.
Eliminate one roundtrip -> external CSS ❌

`Is NOT beneficial if the file (HTML + CSS section) is very long`

Could use both internal + external

- Some styling will load immediately with HTML file
- The rest will load with external CSS file

```CSS
display: inline-block
```

![alt text](image-4.png)

Inline elements doesn't respect height + width

![alt text](image.png)

## Inline-Block

Combination of block + inline

- Respects height + width
- Side by Side (if there is enough space)
- Stacked (Not enough space)

![alt text](image-2.png)

## Flex

We want it to work, regardless of the space.
HERO: `flex`

- flex is a master of distributing empty space (when you fix width for each box)

- Apply on parent element (not on child):
  - Applied on outer box (.container) -> not inner boxes (.box1, .box2, .box3)

ALWAYS side by side:
![alt text](image-3.png)

flex tries to `keep the height constant` -> more width is given to more wording (i.e., middle section compared to first).
extra info: flex-shrink will determine how fast it shrinks



` click box next to display: flex to choose between empty space usage`

![alt text](image-7.png)

default:

![alt text](image-5.png)

justify-content: center

![alt text](image-6.png)

- flex broke up the empty space and distributed it to each side

space-evenly vs space around:

space even has even space for every gap

space around has even space on the inside and on the outside the space is even on either side but it is half of the inside

### align-items: center

![alt text](image-8.png)

aligns content vertically/arranging boxes, in resp
stretch is default

### flex-direction

Used to stack content
