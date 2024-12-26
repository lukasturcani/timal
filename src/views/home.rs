use crate::components::Hero;
use dioxus::prelude::*;

#[component]
pub fn Home() -> Element {
    rsx! {
        Hero {}
        div {
            class: "bg-red-500 p-4 text-center dark:bg-green-500",
            "Hello, world!"
        }

    }
}
