
print("Enter your problems (comma separated):")
user_input = input().lower()

facts = set([f.strip().replace(" ", "_") for f in user_input.split(",")])

rules = [
    ({"engine_not_starting", "battery_low"}, "battery_issue"),
    ({"battery_issue"}, "replace_battery"),
    ({"engine_not_starting", "fuel_empty"}, "refill_fuel"),
    ({"engine_overheating"}, "cool_engine"),
    ({"low_oil_level"}, "add_engine_oil"),
]
problems = {"battery_issue"}
solutions = {"replace_battery", "refill_fuel", "cool_engine", "add_engine_oil"}

derived = set()
logs = []

changed = True
while changed:
    changed = False
    for condition, result in rules:
        if condition.issubset(facts) and result not in facts:
            facts.add(result)
            derived.add(result)
            logs.append(f"Rule applied: {condition} -> {result}")
            changed = True

print("\n Detected Problems:")
found_problem = False
for f in derived:
    if f in problems:
        print("-", f.replace("_", " "))
        found_problem = True

if not found_problem:
    print("No major problem detected")

print("\n Suggested Solutions:")
found_solution = False
for f in derived:
    if f in solutions:
        print("-", f.replace("_", " "))
        found_solution = True

if not found_solution:
    print("No solution available")

print("\n Reasoning Steps:")
for log in logs:
    print(log)