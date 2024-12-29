use crate::components::Dropzone;
use dioxus::prelude::*;
use serde::{Deserialize, Serialize};
use std::path::PathBuf;

#[derive(Copy, Clone, PartialEq, Eq)]
enum State {
    WaitingForWebSocket,
    NoFiles,
    HasFiles,
}

#[component]
pub fn Analysis() -> Element {
    let state = use_signal(|| State::WaitingForWebSocket);
    let files = use_resource(|| async {
        let domain = document::eval("return document.domain;")
            .await
            .unwrap()
            .to_string();
        tracing::info!("domain is {domain}");
        files()
    });
    rsx! {
        main {
            class: "container mx-auto min-h-screen flex items-center justify-center",
            Dropzone {
                onchange: move |e: FormEvent| {
                    tracing::info!("File changed");
                }
            }

        }
    }
}

#[derive(Clone, PartialEq, Eq)]
struct FileData {
    name: String,
    path: PathBuf,
}

async fn files() -> Vec<FileData> {
    todo!()
}
