tuple product{key string name; int demand; float inside; float outside;};
tuple resource{key string name; int capacity;};
tuple consumption {key string product; key string resource; int capacity;};
{product} products = ...;
{resource} resources = ...;
{consumption} consumptions = ...;
dvar float+ inside_vars[products];
dvar float+ outside_vars[products];
dexpr float total_inside_cost = sum(p in products) inside_vars[p] * p.inside;
dexpr float total_outside_cost = sum(p in products) outside_vars[p] * p.outside;
dvar float obj;

minimize(obj);
subject to{
forall(p in products) inside_vars[p] + outside_vars[p] >= p.demand;
forall(res in resources) sum(p in products) inside_vars[p] * item(consumptions,<p.name, res.name>).capacity  <= res.capacity;
    obj == total_inside_cost + total_outside_cost;
}

tuple sol{ float obj; float inside; float outside;};
sol solution = <obj, total_inside_cost, total_outside_cost>;
