const py = @import("pydust");

pub fn add(args: struct { a: i32, b: i32 }) i32 {
    return args.a + args.b;
}

comptime {
    py.rootmodule(@This());
}
