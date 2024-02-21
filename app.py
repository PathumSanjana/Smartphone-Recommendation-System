from typing import Any
from fuzzywuzzy import process
from h2o_wave import Q, main, app, ui
from typing import Any, List, Tuple

# Mock smartphone data for demonstration
smartphone_names = [
    "iPhone 13",
    "Samsung Galaxy S21",
    "Google Pixel 6",
    "OnePlus 9 Pro",
    "Xiaomi Mi 11",
    "Sony Xperia 1 III",
    "Huawei P50 Pro",
    "LG Velvet",
    "Motorola Edge+",
    "Asus ROG Phone 5"
]

def search_smartphones(smartphone_name: str) -> List[Tuple[str, Any]]:
    """
    Find similar smartphones name wise (using Levenshtein distance).
    """
    return process.extract(smartphone_name, smartphone_names)

@app("/smartphone-recommender")
async def serve(q: Q):
    """
    Displays the recommended smartphones according to the input.
    If the user cannot find the smartphone, user can find the smartphones that matches to the given input.
    """
    msg = ""

    if not q.client.initialized:
        q.client.initialized = True

    if q.args.search:
        del q.page["smartphones"]
        q.args.search_box_input = q.args.search_box_input.strip()
        if q.args.search_box_input in smartphone_names:
            result = search_smartphones(q.args.search_box_input)
            msg = f"If you like {q.args.search_box_input}, you may also like these!"
            add_smartphone_cards(result, q)
        elif not q.args.search_box_input:
            msg = "Smartphone name cannot be blank."
        else:
            msg = f'"{q.args.search_box_input}" is not in our database or an invalid smartphone name. \
                    Use the "Find Smartphone" button to find smartphones.'

    if q.args.find_smartphones:
        q.args.search_box_input = q.args.search_box_input.strip()
        if not q.args.search_box_input:
            msg = "Smartphone name cannot be blank."
        else:
            for i in range(1, 6):
                del q.page[f"smartphone{i}"]
            add_similar_smartphones(q)

    add_search_box(q, msg)
    add_header(q)
    add_footer(q)

    await q.page.save()

def add_similar_smartphones(q: Q):
    similar_smartphones = search_smartphones(q.args.search_box_input)
    q.page["smartphones"] = ui.form_card(
        box="2 4 10 7",
        items=[
            ui.copyable_text(
                value=smartphone[0],
                name=f"smartphone_match{i+1}",
                label=f"{smartphone[1]}% match",
            )
            for i, smartphone in enumerate(similar_smartphones)
        ],
    )

def add_header(q: Q):
    q.page["header"] = ui.header_card(
        box="2 1 10 1",
        title="Smartphone Recommendation System",
        subtitle="Find smartphones similar to the ones you like!",
        icon="Smartphone",
        items=[
            ui.link(
                name="github_btn",
                path="https://github.com/example/smartphone-recommendation-system",
                label="GitHub",
                button=True,
            )
        ],
    )

def add_smartphone_cards(result, q: Q):
    for i in range(1, 6):
        q.page[f"smartphone{i}"] = ui.tall_article_preview_card(
            box=f"{2*i} 4 2 7",
            title=f"{result[i-1][0]}",
            subtitle="",
            value="",
            name="tall_article",
            image="https://via.placeholder.com/150",
            items=[
                ui.text(f"Manufacturer: {result[i-1][0].split()[0]}", size="l"),
                ui.text(f"Model: {result[i-1][0].split(maxsplit=1)[1]}", size="m"),
            ],
        )

def add_search_box(q: Q, msg):
    q.page["search_box"] = ui.form_card(
        box="2 2 10 2",
        items=[
            ui.textbox(
                name="search_box_input",
                label="Smartphone Name",
                value=q.args.search_box_input,
            ),
            ui.buttons(
                items=[
                    ui.button(
                        name="search",
                        label="Search",
                        primary=True,
                        icon="Search",
                    ),
                    ui.button(name="find_smartphones", label="Find Smartphone", primary=False),
                ]
            ),
            ui.text(msg, size="m", name="msg_text"),
        ],
    )

def add_footer(q: Q):
    caption = """__Made with 💛 by Your Name__ <br /> using __[h2o Wave](https://wave.h2o.ai/docs/getting-started).__"""
    q.page["footer"] = ui.footer_card(
        box="2 11 10 2",
        caption=caption,
        items=[
            ui.inline(
                justify="end",
                items=[
                    ui.links(
                        label="Contact Me",
                        width="200px",
                        items=[
                            ui.link(
                                name="github",
                                label="GitHub",
                                path="https://github.com/example/smartphone-recommendation-system",
                                target="_blank",
                            ),
                            ui.link(
                                name="linkedin",
                                label="LinkedIn",
                                path="https://www.linkedin.com/in/yourprofile/",
                                target="_blank",
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )

if __name__ == '__main__':
    main('/smartphone-recommender')
