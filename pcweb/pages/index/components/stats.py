import reflex as rx
#from .pricing import pricing_cards

github_url = "https://github.com/reflex-dev/reflex"
features_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen"
contribution_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22"
bugs_url="https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue"


def user_count_item(count, platform) -> rx.Component:
    return rx.flex(
        rx.text(f"{count}+", color="#E8E8F4", font_size="32px"),
        rx.text(platform, color="#6C6C81"),
        direction="column",
        align="center",
    )

def user_count_comp() -> rx.Component:
    return rx.center(
        rx.tablet_and_desktop(user_count_item("25K", "Profiles Analysed.")),
        rx.mobile_only(user_count_item("25K", "Profiles Analysed.")),
        rx.divider(size="4", orientation="vertical"),
        rx.tablet_and_desktop(user_count_item("80K", "Profiles Unfollowed.")),
        rx.mobile_only(user_count_item("80K", "Profiles Unfollowed.")),
        rx.divider(size="4", orientation="vertical"),
        rx.tablet_and_desktop(user_count_item("10K", "Active Members.")),
        rx.mobile_only(user_count_item("10K", "Active Members.")),
        spacing="5",
        padding="1em",
    )


def pricing_badge() -> rx.Component:
    return rx.button(
        rx.flex(
            rx.text(
                "Pricing Plans",
                color="transparent",
                font_size="14px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.28px",
                background="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                background_clip="text",
                _webkit_background_clip="text",
            ),
            height="31px",
            padding="0px 10px",
            justify="center",
            align="center",
            gap="10px",
            border_radius="15px",
            border="1px solid #4435D4",
            background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
            box_shadow="0px 0px 4px -1px rgba(27, 21, 90, 0.40), 0px 3px 6px -3px rgba(34, 25, 121, 0.60);",
        ),
        background="transparent",
        on_click=rx.redirect(
            github_url,
            external=True,
        ),
        _hover={
            "cursor": "pointer",
        },
    )

def instagram_button() -> rx.Component:
    return rx.button(
        rx.flex(
            rx.image(src="/companies/light/instagram.svg", height="20px", width="20px"),
            rx.center(
                "Instagram",
                color="#FFFFFF",
                font_size="14px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.28px",
            ),
            rx.center(
                "1000",
                color="#6151F3",
                font_size="12px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.24px",
            ),
            spacing="2",
        ),

        position="relative",
        top="32px",
        right="-140px",
        z_index="999",
        padding="var(--Space-4, 16px);",
        align="center",
        width="151px",
        height="42px",
        border_radius="70px",
        border="1px solid #3C3646",
        background="linear-gradient(243deg, #16141A -74.32%, #222029 69.37%);",
        box_shadow="0px 0px 27px -4px rgba(0, 0, 0, 0.30);",
        on_click=rx.redirect(
            github_url,
            external=True,
        ),
        _hover={
            "cursor": "pointer",
        },
    )

def invite_message() -> rx.Component:
    return rx.box(
        rx.text(
            "Analytics is free from Us. Just pay for other Feature's.",
            color="#D6D6ED",
            font_size="38px",
            weight="bold",
            align="center",
            line_height="1",
        ),
        width="30em",
    )

def request_buttons() -> rx.Component:
    return rx.hstack(
        rx.button(
            "Followers",
            color="#2BCEEA",
            weight="Medium",
            height="24px",
            width="138px",
            border="1px solid #2BCEEA",
            background_color="rgba(43, 206, 234, 0.25)",
            on_click=rx.redirect(
                bugs_url,
                external=True,
            ),
            _hover={
                "cursor": "pointer",
            },
        ),
        rx.button(
            "Following",
            color="#2BEA8E",
            weight="Medium",
            height="24px",
            border="1px solid #2BEA8E",
            background_color="rgba(43, 234, 142, 0.25)",
            on_click=rx.redirect(
                contribution_url,
                external=True,
            ),
            _hover={
                "cursor": "pointer",
            },
        ),
        rx.button(
            "Not Following",
            color="#2BCEEA",
            weight="Medium",
            height="24px",
            border="1px solid #2BCEEA",
            background_color="rgba(43, 234, 142, 0.25)",
            on_click=rx.redirect(
                contribution_url,
                external=True,
            ),
            _hover={
                "cursor": "pointer",
            },
        ),
    )

def invite_card_comp() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.text(
                "Analyse Your Instagram!", 
                color="#D6D6ED",
                weight="medium",
            ),
            request_buttons(),
            rx.text(
                "Start Today, Login for More Details",
                color="#6C6C81",
                weight="medium",
            ),
            justify="start",
            direction="column",
            spacing="2",
        ),
        border_radius="10px",
        padding="1em",
        width="30em",
        border="1px solid #3C3646;",
        background="linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%);",
        box_shadow= "0px 27px 44px -13px rgba(214, 214, 237, 0.10) inset, 0px 0px 27px -4px rgba(0, 0, 0, 0.30);",
    )

def check_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon("check",  size=18, color="cyan"),
        rx.text(text, size="4"),
    )

def no_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon("octagon-x", size=18, color="crimson"),
        rx.text(text, size="4"),
    )


def free_features() -> rx.Component:
    return rx.vstack(
        check_item("Analyse Account 1/Day."),
        check_item("Analyse folloing 1/Day."),
        check_item("Analyse Post's 1/Day."),
        no_item("Unfollow User's 5/Day."),
        no_item("Advanced analytics."),
        no_item("Daily backups."),
        no_item("Real-time Updates."),
        width="100%",
        align_items="start",
    )


def basic_features() -> rx.Component:
    return rx.vstack(
        check_item("Analyse Account 99/Day."),
        check_item("Analyse folloing 99/Day."),
        check_item("Analyse Post's 99/Day."),
        check_item("Unfollow User's 500/Day."),
        check_item("Advanced analytics."),
        no_item("Daily backups."),
        no_item("Real-time Updates."),
        width="100%",
        align_items="start",
    )

def premium_features() -> rx.Component:
    return rx.vstack(
        check_item("Analyse Account 500/Day."),
        check_item("Analyse folloing 500/Day."),
        check_item("Analyse Post's 500/Day."),
        check_item("Unfollow User's 1500/Day."),
        check_item("Advanced analytics."),
        check_item("Daily backups."),
        check_item("Real-time Updates."),
        width="100%",
        align_items="start",
    )


def pricing_card_free() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.badge("Free", weight="bold", size="3", radius="full",variant="surface",color_scheme="gray"),
            rx.text(
                "Ideal choice for personal profile Analytics.",
                size="4",
                opacity=0.8,
                align="center",
            ),
            rx.hstack(
                rx.text(
                    "₹0",
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
            rx.badge("Basic", weight="bold", size="3", radius="full",variant="surface",color_scheme="indigo"),
            rx.text(
                "Ideal choice for personal profile Analytics.",
                size="4",
                opacity=0.8,
                align="center",
            ),
            rx.hstack(
                rx.text(
                    "₹350",
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
            rx.badge("Premium", weight="bold", size="3", radius="full",variant="surface",color_scheme="crimson"),
            rx.text(
                "Ideal choice for personal profile Analytics.",
                size="4",
                opacity=0.8,
                align="center",
            ),
            rx.hstack(
                rx.text(
                    "₹850",
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


def stats() -> rx.Component:
    return rx.vstack(
        pricing_badge(),
        invite_message(),
        pricing_cards(),
        instagram_button(),
        invite_card_comp(),
        user_count_comp(),
        padding="2em",
        style={
            "@media screen and (max-width: 1024px)": {
                "transform": "scale(0.9)",
            },
            "@media screen and (max-width: 837px)": {
                "transform": "scale(0.85)",
            },
            "@media screen and (max-width: 768px)": {
                "transform": "scale(0.8)",
            },
            "@media screen and (max-width: 627px)": {
                "transform": "scale(0.75)",
            },
            "@media screen and (max-width: 480px)": {
                "transform": "scale(0.65)",
            },
        },
    )