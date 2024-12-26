use crate::components::Dropzone;
use dioxus::prelude::*;

#[component]
pub fn Analysis() -> Element {
    rsx! {
        Dropzone {}
    }
}
