import os
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class ZigBuilder(build_ext):
    def build_extension(self, ext):
        assert len(ext.sources) == 1

        if not os.path.exists(self.build_lib):
            os.makedirs(self.build_lib)
        self.spawn(
            [
                "zig",
                "build-lib",
                "-O",
                "ReleaseFast",
                "-lc",
                f"-femit-bin={self.get_ext_fullpath(ext.name)}",
                "-fallow-shlib-undefined",
                "-dynamic",
                *[f"-I{d}" for d in self.include_dirs],
                ext.sources[0],
            ]
        )


setup(
    name="hellozig",
    version="0.0.1",
    description="a experiment create Python module in Zig",
    ext_modules=[
        Extension("hellozig", sources=["hellomodule.zig"])
    ],
    cmdclass={"build_ext": ZigBuilder},
)
