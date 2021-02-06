class GenerateHTML:
    @staticmethod
    def generate_file_window_tree(paths):
        html_code = r'<div class="tree">'
        html_code = recution_file_window(paths, html_code)
        html_code += r'</div>'
        return html_code


def recution_file_window(paths, html_code):
    for folder, items in paths.items():
        if items == {}:
            html_code += \
                rf'<label class="tree-item item"><input class="tree-cb" type="radio" name="item"><span class="tree-label">{folder}</span></label>'
        else:
            html_code += rf'<label class="tree-item item"><input class="tree-cb" type="checkbox"><span class="tree-label">{folder}</span><div class="tree-branches">'
            html_code = recution_file_window(items, html_code)
            html_code += rf'</div></label>'
    return html_code
