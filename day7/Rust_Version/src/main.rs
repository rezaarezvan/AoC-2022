use anyhow::Result;

fn main() -> Result<()> {
    let input = std::fs::read_to_string("input")?;

    let mut stack = vec![("/", 0)];

    let mut final_stack = vec![];

    let total_space = 70000000;

    let space_del = 30000000;

    let report = 100_000;
    let mut total = 0;

    for line in input.lines().filter(|l| !l.is_empty()) {
        if line == "$ cd /" || line == "$ ls" {
            continue;
        }

        if line.starts_with("$ cd ") {
            let dir = &line[5..];
            if dir == ".." {
                let (name, amount) = stack.pop().unwrap();
                if amount <= report {
                    total += amount;
                }
                stack.last_mut().unwrap().1 += amount;
                final_stack.push((name, amount));
            } else {
                stack.push((dir, 0));
            }
            continue;
        }

        let (amount, _) = line.split_once(" ").unwrap();

        if let Ok(amount) = amount.parse::<usize>() {
            stack.last_mut().unwrap().1 += amount;
        } else if amount == "dir" {
            // Ignore
        }
    }

    while stack.len() > 0 {
        let (name, amount) = stack.pop().unwrap();
        final_stack.push((name, amount));

        if stack.len() > 0 {
            stack.last_mut().unwrap().1 += amount;
        }
    }

    let free_space = total_space - final_stack.last().unwrap().1;

    let space_req = space_del - free_space;

    let total = final_stack
        .into_iter()
        .filter(move |(_, amount)| *amount >= space_req)
        .map(|(name, amount)| return amount)
        .min();

    println!("{:?}", total);

    return Ok(());
}
