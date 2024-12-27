use crate::components::Dropzone;
use dioxus::prelude::*;
use futures_util::{SinkExt, StreamExt};
use serde::{Deserialize, Serialize};
use std::{cell::RefCell, path::PathBuf, rc::Rc};

use tokio_tungstenite_wasm::connect;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
struct AddFile {
    name: String,
    path: PathBuf,
    xs: Vec<f64>,
    ys: Vec<f64>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
#[serde(tag = "type")]
enum Command {
    AddFile(AddFile),
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
struct Message {
    command: Command,
}

#[component]
pub fn Analysis() -> Element {
    let client = use_resource(|| async {
        Rc::new(RefCell::new(
            connect("ws://localhost:8000/ws").await.unwrap(),
        ))
    });
    rsx! {
        main {
            class: "container mx-auto min-h-screen flex items-center justify-center",
            Dropzone {
                onchange: move |e: FormEvent| {
                    tracing::info!("File changed");
                    spawn(async move {
                        if let Some(client) = &*client.read() {
                            let msg = Message {
                                command: Command::AddFile(AddFile {
                                    name: "test".to_string(),
                                    path: PathBuf::from("/Users/lukas/projects/timal/add-websockets/backend/src/millie/main.py"),
                                    xs: vec![1.0, 2.0, 3.0],
                                    ys: vec![1.0, 2.0, 3.0],
                                }),
                            };
                            let json = serde_json::to_vec(&msg).unwrap();
                            client.borrow_mut().send(json.into()).await.unwrap();
                        }
                    });
                }
            }

        }
    }
}
