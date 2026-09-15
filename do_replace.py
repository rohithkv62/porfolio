import sys

html_file = r"c:\porfolio-website\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace CSS
start_str = "    .clean-loader {\n      display: flex;"
end_str = "    .cl-dot.active {\n      background: #00e5ff;\n      box-shadow: 0 0 10px #00e5ff;\n      transform: scale(1.2);\n    }"

start_idx = content.find(start_str)
end_idx = content.find(end_str) + len(end_str)

new_css = """    .loader {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      width: 100vw;
    }

    .loader svg {
      width: 100%;
      height: 100px;
    }

    .loader text {
      font-size: 48px;
      font-weight: bold;
      fill: none;
      stroke: #00ffcc;
      stroke-width: 2;
    }

    /* Your animation reused */
    .dash {
      animation: dashArray 2s ease-in-out infinite,
                 dashOffset 2s linear infinite;
    }

    .spin {
      animation: spinDashArray 2s ease-in-out infinite,
                 spin 8s ease-in-out infinite,
                 dashOffset 2s linear infinite;
      transform-origin: center;
    }

    @keyframes dashArray {
      0% {
        stroke-dasharray: 0 1 359 0;
      }
      50% {
        stroke-dasharray: 0 359 1 0;
      }
      100% {
        stroke-dasharray: 359 1 0 0;
      }
    }

    @keyframes spinDashArray {
      0% {
        stroke-dasharray: 270 90;
      }
      50% {
        stroke-dasharray: 0 360;
      }
      100% {
        stroke-dasharray: 270 90;
      }
    }

    @keyframes dashOffset {
      0% {
        stroke-dashoffset: 365;
      }
      100% {
        stroke-dashoffset: 5;
      }
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(1080deg); }
    }"""

if start_idx != -1 and content.find(end_str) != -1:
    content = content[:start_idx] + new_css + content[end_idx:]
else:
    print("Could not find CSS block!")
    sys.exit(1)


# 2. Replace HTML
start_html_str = '    <div class="clean-loader">'
end_html_str = '            <span class="cl-dot"></span>\n        </div>\n    </div>'

start_html_idx = content.find(start_html_str)
end_html_idx = content.find(end_html_str) + len(end_html_str)

new_html = """    <div class="loader">
      <svg viewBox="0 0 600 100" class="w-100">
        <text
          x="50%"
          y="50%"
          text-anchor="middle"
          dominant-baseline="middle"
          class="dash spin"
        >
          ROHITH K V..
        </text>
      </svg>
    </div>"""

if start_html_idx != -1 and content.find(end_html_str) != -1:
    content = content[:start_html_idx] + new_html + content[end_html_idx:]
else:
    print("Could not find HTML block!")
    sys.exit(1)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
