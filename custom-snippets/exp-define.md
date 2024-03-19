::: {.cell .markdown}
### Define configuration for this experiment (two hosts on a LAN)
:::

::: {.cell .code}
```python
slice_name="sockets_python-" + fablib.get_bastion_username()

node_conf = [
 {'name': "romeo",   'cores': 1, 'ram': 2, 'disk': 10, 'image': 'default_ubuntu_22', 'packages': ["python3"]}, 
 {'name': "juliet",  'cores': 1, 'ram': 2, 'disk': 10, 'image': 'default_ubuntu_22', 'packages': ["python3"]}, 
]
net_conf = [
 {"name": "net", "subnet": "10.10.0.0/24", "nodes": [{"name": "romeo",   "addr": "10.10.0.100"}, {"name": "juliet", "addr": "10.10.0.101"}]}
]
route_conf = []
exp_conf = {'cores': sum([ n['cores'] for n in node_conf]), 'nic': sum([len(n['nodes']) for n in net_conf]) }
```
:::
