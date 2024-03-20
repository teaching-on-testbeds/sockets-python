all: start_here_fabric.ipynb start_here_chi.ipynb

clean:
	rm start_here_fabric.ipynb start_here_chi.ipynb

FAB := fabric-snippets/fab-config.md fabric-snippets/reserve-resources.md fabric-snippets/configure-resources.md fabric-snippets/offload-off.md fabric-snippets/draw-topo-detailed-labels.md fabric-snippets/log-in.md fabric-snippets/delete-slice.md
CHI := chameleon-snippets/chi-config.md chameleon-snippets/reserve-resources.md chameleon-snippets/configure-resources.md chameleon-snippets/offload-off.md chameleon-snippets/draw-topo-detailed-labels.md chameleon-snippets/log-in.md chameleon-snippets/delete-slice.md

start_here_fabric.ipynb: $(FAB) custom-snippets/intro.md custom-snippets/exp-define-fabric.md 
	pandoc --wrap=none \
                -i custom-snippets/intro.md fabric-snippets/fab-config.md \
                custom-snippets/exp-define-fabric.md \
                fabric-snippets/reserve-resources-eduky.md fabric-snippets/configure-resources.md \
				fabric-snippets/offload-off.md \
				fabric-snippets/draw-topo-detailed-labels.md fabric-snippets/log-in.md \
				fabric-snippets/delete-slice.md \
                -o start_here_fabric.ipynb  

start_here_chi.ipynb: $(CHI) custom-snippets/intro.md custom-snippets/exp-define-chi.md
	pandoc --wrap=none \
                -i custom-snippets/intro.md chameleon-snippets/chi-config.md \
                                custom-snippets/exp-define-chi.md \
                                chameleon-snippets/configure-resources.md \
                                chameleon-snippets/offload-off.md \
                                chameleon-snippets/draw-topo-detailed-labels.md \
                                chameleon-snippets/log-in.md \
                                chameleon-snippets/delete-slice.md \
                -o start_here_chi.ipynb

