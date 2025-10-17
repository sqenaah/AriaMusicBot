utf-8utf-8





















importasyncio
importshlex
fromtypingimportTuple

fromgitimportRepo
fromgit.excimportGitCommandError,InvalidGitRepositoryError

importconfig

from..loggingimportLOGGER


definstall_req(cmd:str)->Tuple[str,str,int,int]:
    asyncdefinstall_requirements():
        args=shlex.split(cmd)
process=awaitasyncio.create_subprocess_exec(
*args,
stdout=asyncio.subprocess.PIPE,
stderr=asyncio.subprocess.PIPE,
)
stdout,stderr=awaitprocess.communicate()
return(
stdout.decode("utf-8","replace").strip(),
stderr.decode("utf-8","replace").strip(),
process.returncode,
process.pid,
)

returnasyncio.get_event_loop().run_until_complete(install_requirements())


defgit():
    REPO_LINK=config.UPSTREAM_REPO
ifconfig.GIT_TOKEN:
        GIT_USERNAME=REPO_LINK.split("com/")[1].split("/")[0]
TEMP_REPO=REPO_LINK.split("https://")[1]
UPSTREAM_REPO=f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
else:
        UPSTREAM_REPO=config.UPSTREAM_REPO
try:
        repo=Repo()
LOGGER(__name__).info(f"Git Client Found [VPS DEPLOYER]")
exceptGitCommandError:
        LOGGER(__name__).info(f"Invalid Git Command")
exceptInvalidGitRepositoryError:
        repo=Repo.init()
if"origin"inrepo.remotes:
            origin=repo.remote("origin")
else:
            origin=repo.create_remote("origin",UPSTREAM_REPO)
origin.fetch()
repo.create_head(
config.UPSTREAM_BRANCH,
origin.refs[config.UPSTREAM_BRANCH],
)
repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
origin.refs[config.UPSTREAM_BRANCH]
)
repo.heads[config.UPSTREAM_BRANCH].checkout(True)
try:
            repo.create_remote("origin",config.UPSTREAM_REPO)
exceptBaseException:
            pass
nrs=repo.remote("origin")
nrs.fetch(config.UPSTREAM_BRANCH)
try:
            nrs.pull(config.UPSTREAM_BRANCH)
exceptGitCommandError:
            repo.git.reset("--hard","FETCH_HEAD")
install_req("pip3 install --no-cache-dir -r requirements.txt")
LOGGER(__name__).info(f"Fetching updates from upstream repository...")












