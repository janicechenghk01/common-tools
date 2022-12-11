#Initial Setup for a laptop
Install the following tools with homebrew
- openjdk: `brew install openjdk`
- python: `brew install python`
- scala: `brew install scala`
- pycharm-ce: `brew install --cask pycharm-ce`
- iterm2: `brew install iterm2`
- awscli: `brew install awscli`
- [kubectl](https://minikube.sigs.k8s.io/docs/start/): `brew install kubectl`
- minikube: `brew install minikube` 
- kubens: `brew install kubens`
- k9s: `brew install derailed/k9s/k9s`
- git: `brew install git`
- sqlworkbenchj: `brew install --cask sqlworkbenchj`


## k9s
1. Define the XDG_CONFIG_HOME path: `export XDG_CONFIG_HOME=$HOME/.config`
2. Download [skin](https://github.com/derailed/k9s/tree/master/skins) from k9s repo and move to the `$XDG_CONFIG_HOME/k9s/`
```bash
cd init-setup
cp ./colors/rose-pine-k9s.yml $XDG_CONFIG_HOME/k9s/skin.yml
```
