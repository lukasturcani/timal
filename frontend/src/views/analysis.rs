use crate::components::Dropzone;
use dioxus::prelude::*;
use futures_util::{SinkExt, StreamExt};
use std::{cell::RefCell, rc::Rc};

use tokio_tungstenite_wasm::connect;

#[component]
pub fn Analysis() -> Element {
    let client = use_resource(|| async {
        Rc::new(RefCell::new(
            connect("ws://localhost:8000/ws").await.unwrap(),
        ))
    });
    rsx! {
        Dropzone {
            onchange: move |e: FormEvent| {
                tracing::info!("File changed");
                spawn(async move {
                    if let Some(client) = &*client.read() {
                        let msg = &b"hello"[..];
                        client.borrow_mut().send(msg.into()).await.unwrap();
                    }
                });
            }
        }
    }
}
