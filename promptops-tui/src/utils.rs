use glob::glob;
use std::fs;
use std::path::PathBuf;

pub fn resolve_file_injection(val: &str) -> String {
    if !val.starts_with('@') {
        return val.to_string();
    }

    let pattern = &val[1..];
    let mut contents = Vec::new();
    let mut files = Vec::<PathBuf>::new();

    if let Ok(entries) = glob(pattern) {
        for entry in entries.filter_map(Result::ok) {
            if entry.is_file() {
                files.push(entry);
            }
        }
    }

    if files.is_empty() {
        return val.to_string();
    }

    files.sort();

    for f_path in &files {
        if let Ok(content) = fs::read_to_string(f_path) {
            let content = content.trim();
            if files.len() > 1 {
                contents.push(format!("--- File: {} ---\n{}", f_path.display(), content));
            } else {
                contents.push(content.to_string());
            }
        }
    }

    if contents.is_empty() {
        val.to_string()
    } else {
        contents.join("\n\n")
    }
}
