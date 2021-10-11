//! # ST

// \ allow
#![allow(dead_code)]
#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
#![allow(non_upper_case_globals)]
// / allow

// \ mod
mod test;
// / mod

// \ extern
extern crate tracing;
// / extern

// \ use
use tracing::{info, instrument};
// / use

#[instrument]
/// program entry point
fn main() {
    tracing_subscriber::fmt().compact().init();
    // \ args
    let argv: Vec<String> = std::env::args().collect();
    let argc = argv.len();
    let program = std::path::Path::new(&argv[0]);
    let module = program.file_stem().unwrap();
    info!("start {:?} as #{:?} {:?}", module, argc, argv);
    // / args
    // \ atexit
    info!("stop");
    // / atexit
}
