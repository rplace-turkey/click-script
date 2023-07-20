# based on works of tux (linux mascot) folks (https://github.com/ryleu/tux-on-place)
# humanova 2022
# github.com/rplace-turkey

import matplotlib.pyplot as plt

imgpath = "images/bayrak.png"
outputpath = "pages/bayrak.html"
coordinate_x = -368
coordinate_y = 325


ui_scale = 8


def generate_static_webpage(image_path: str, output_filename: str, top_left: tuple):
    generated = ""
    number = 1
    p = plt.imread(image_path)
    for row in range(len(p)):
        generated += f"<div class='row' style='top: {row * ui_scale}px;'>"
        for square in range(len(p[row])):
            print(f"Processing: {number}")
            number += 1
            color = f"rgba({p[row][square][0]*255},{p[row][square][1]*255},{p[row][square][2]*255},{p[row][square][3]})"
            hide_transparent_tile_css = "pointer-events: none" if p[row][square][3] == 0 else ""
            generated += f"<a style='background-color: {color};left: {square * ui_scale}px; {hide_transparent_tile_css}' class='square' href='https://new.reddit.com/r/place/?cx={top_left[0] + square}&cy={top_left[1] + row}&px=20' onMouseOver='onTileHovered({square}, {row })'></a>\n"
        generated += "</div>"

    website_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <style>
    * {{
        top: 0;
        left: 0;
        padding: 0;
        margin: 0;
        width: {ui_scale}px;
        height: {ui_scale}px;
    }}
    .row {{
        position: absolute;
        width: {ui_scale * len(p[0])}px;
    }}
    .square {{
        position: absolute;
    }}
    .square:hover {{
        z-index: 1;
        border: solid 1px black;
        outline: solid 1px white;
    }}
    .info{{
        color: black;
        position: absolute;
        background-color: white;
        font-family: monospace;
        z-index: 2;
        border-radius: 8px;
        height: 20px;
        font-size: 16px;
        width: 100px;
        pointer-events: none;
        text-align: center;
        border: solid 1px black;
        outline: solid 1px white;
    }}
    </style>
    
    <script>
        function onTileHovered(x, y) {{
        const pos = document.getElementById("pos");
        pos.innerText = "[" + (x + { top_left[0] }) + ", " + (y + {top_left[1]}) + "]";
        pos.style.left = x * {ui_scale} + 16 + "px";
        pos.style.top = y * {ui_scale} - 6 + "px";
      }}
    </script>

    <body style="background-color:#1a1919">
    <div id="pos" class="info">[999,999]</div> 
    <div>
    {generated}
    </div>
    </body>
    </html>
    """

    with open(f"{output_filename}", "w") as file:
        file.write(website_template)


if __name__ == '__main__':
    generate_static_webpage(image_path=f"{imgpath}",
                            output_filename=f"{outputpath}",
                            top_left=(coordinate_x, coordinate_y))
