utf-8utf-8





















importglob
fromos.pathimportdirname,isfile


def__list_all_modules():
    work_dir=dirname(__file__)
mod_paths=glob.glob(work_dir+"/*/*.py")

all_modules=[
(((f.replace(work_dir,"")).replace("/","."))[:-3])
forfinmod_paths
ifisfile(f)andf.endswith(".py")andnotf.endswith("__init__.py")
]

returnall_modules


ALL_MODULES=sorted(__list_all_modules())
__all__=ALL_MODULES+["ALL_MODULES"]












