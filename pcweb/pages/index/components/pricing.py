import reflex as rx

def check_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon("check", size=18, color="cyan"),
        rx.text(text, size="4"),
    )

def no_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon("octagon-x", size=18, color="crimson"),
        rx.text(text, size="4"),
    )


def free_features() -> rx.Component:
    return rx.vstack(
        check_item("Analyse your Instagram Account. Once Per Day."),
        check_item("Analyse User's who are folloing. Once Per Day."),
        check_item("Analyse Users' you are Following. Once Per Day."),
        no_item("Unfollow User's Not-Following Back."),
        no_item("Advanced analytics."),
        no_item("Daily backups."),
        no_item("Real-time Updates."),
        width="100%",
        align_items="start",
    )


def basic_features() -> rx.Component:
    return rx.vstack(
        check_item("Analyse your Instagram Account. Once Per Day."),
        check_item("Analyse User's who are folloing. Once Per Day."),
        check_item("Analyse Users' you are Following. Once Per Day."),
        check_item("Unfollow User's."),
        no_item("Advanced analytics."),
        check_item("Daily backups."),
        check_item("Real-time Updates."),
        width="100%",
        align_items="start",
    )

def premium_features() -> rx.Component:
    return rx.vstack(
        check_item("Analyse your Instagram Account. Once Per Day."),
        check_item("Analyse User's who are folloing. Once Per Day."),
        check_item("Analyse Users' you are Following. Once Per Day."),
        check_item("Unfollow User's Not-Following Back."),
        check_item("Advanced analytics."),
        check_item("Daily backups."),
        check_item("Real-time Updates."),
        width="100%",
        align_items="start",
    )


def pricing_card_free() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.badge("Free", weight="bold", size="3", radius="full",variant="soft",color_scheme="gray"),
            rx.text(
                "Ideal choice for personal profile Analytics.",
                size="4",
                opacity=0.8,
                align="center",
            ),
            rx.hstack(
                rx.text(
                    "$39",
                    weight="bold",
                    font_size="3rem",
                    trim="both",
                ),
                rx.text(
                    "/month",
                    size="4",
                    opacity=0.8,
                    trim="both",
                ),
                width="100%",
                align_items="end",
                justify="center",
            ),
            width="100%",
            align="center",
            spacing="6",
        ),
        free_features(),
        rx.button(
            "Get started",
            size="3",
            variant="solid",
            width="100%",
            color_scheme="blue",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        justify="center",
        border_radius="0.5rem",
    )

def pricing_card_basic() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.badge("Basic", weight="bold", size="3", radius="full",variant="soft",color_scheme="gray"),
            rx.text(
                "Ideal choice for personal profile Analytics.",
                size="4",
                opacity=0.8,
                align="center",
            ),
            rx.hstack(
                rx.text(
                    "$39",
                    weight="bold",
                    font_size="3rem",
                    trim="both",
                ),
                rx.text(
                    "/month",
                    size="4",
                    opacity=0.8,
                    trim="both",
                ),
                width="100%",
                align_items="end",
                justify="center",
            ),
            width="100%",
            align="center",
            spacing="6",
        ),
        basic_features(),
        rx.button(
            "Get started",
            size="3",
            variant="solid",
            width="100%",
            color_scheme="blue",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        justify="center",
        border_radius="0.5rem",
    )

def pricing_card_premium() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.badge("Premium", weight="bold", size="3", radius="full",variant="soft",color_scheme="gray"),
            rx.text(
                "Ideal choice for personal profile Analytics.",
                size="4",
                opacity=0.8,
                align="center",
            ),
            rx.hstack(
                rx.text(
                    "$39",
                    weight="bold",
                    font_size="3rem",
                    trim="both",
                ),
                rx.text(
                    "/month",
                    size="4",
                    opacity=0.8,
                    trim="both",
                ),
                width="100%",
                align_items="end",
                justify="center",
            ),
            width="100%",
            align="center",
            spacing="6",
        ),
        premium_features(),
        rx.button(
            "Get started",
            size="3",
            variant="solid",
            width="100%",
            color_scheme="blue",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        justify="center",
        border_radius="0.5rem",
    )

def pricing_cards() -> rx.Component:
    return rx.flex(
        pricing_card_free(),
        pricing_card_basic(),
        pricing_card_premium(),
        spacing="4",
        flex_direction=["column", "column", "row"],
        width="100%",
        align_items="center",
    )