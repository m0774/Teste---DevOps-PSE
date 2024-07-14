### Abaixo irei deixar todos os scripts criados, a funcionalidade de cada um e como faz para rodar cada um deles. 


remove_redis:

Script feito para apagar todas as chaves 'redis' e 'redisConfig' dos seus aquivos. 
Para rodar o script primeiramente você vai precisar instalar a biblioteca PyYAML usando o seguinte comando no terminal da pasta de scripts: pip install pyyaml
e então utilize o seguinte comando no terminal da pasta de scripts: python remove_redis.py


remove_annotations:

Script feito para apagar a annotations do ingress `nginx.ingress.kubernetes.io/ssl-redirect`. 
Para rodar o script utilize o seguinte comando no terminal da pasta de scripts: python remove_annotations.py


att_version:

Script feito para atualizar a versão de todos Kustomization para `2.2.1`. 
Para rodar o script utilize o seguinte comando no terminal da pasta de scripts: python att_version.py


remove_commits:

Script feito para apagar todos os commits dos seus aquivos. 
Para rodar o script utilize o seguinte comando no terminal da pasta de scripts: python remove_commits.py


remove_duplicate_settings:

Script feito para remover configurações duplicadas.
Para rodar o script primeiramente você vai precisar instalar a biblioteca PyYAML usando o seguinte comando no terminal da pasta de scripts: pip install pyyaml
e então utilize o seguinte comando no terminal da pasta de scripts: python remove_duplicate_settings.py


adjust_order:

Script feito para deixar as configurações na mesma ordem.
Para rodar o script primeiramente você vai precisar instalar a biblioteca PyYAML usando o seguinte comando no terminal da pasta de scripts: pip install pyyaml
e então utilize o seguinte comando no terminal da pasta de scripts: python adjust_order.py


add_env:

Script feito para adicionar a env `ENV:dev`.
Para rodar o script primeiramente você vai precisar instalar a biblioteca PyYAML usando o seguinte comando no terminal da pasta de scripts: pip install pyyaml
e então utilize o seguinte comando no terminal da pasta de scripts: python add_env.py


adjust_containerport:

Script feito para ajustar a containerPort:$PORT;
Para rodar o script primeiramente você vai precisar instalar a biblioteca PyYAML usando o seguinte comando no terminal da pasta de scripts: pip install pyyaml
e então utilize o seguinte comando no terminal da pasta de scripts: python adjust_containerport.py


remove_false:

Script feito para caso uma configuração esteja com `enable: false` remover os demais campos dela
Para rodar o script utilize o seguinte comando no terminal da pasta de scripts: python remove_false.py


adjust_cpu:

Script feito alterar o `requests` e `limits` de CPU para `10m` e `100m`, respectivamente.
Para rodar o script utilize o seguinte comando no terminal da pasta de scripts: python adjust_cpu.py