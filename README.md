# jeecf-cli

## Install

### from PYPI

> pip install jeecf

### from source

```
python -m venv venv
pip install -r requirements.txt
python setup.py install
jeecf version
```

## Commands

### login

```bash
jeecf login <url>
```

### namespace

1. 获取命名空间列表并标出当前命名空间

```bash
jeecf namespace
```

2. 切换命名空间

```bash
jeecf namespace use <name>
```

### dbsource

1. 获取数据源列表并标出当前数据源

```bash
jeecf dbsource
```

2. 切换数据源

```bash
jeecf dbsource use <name>
```

### plugin

1. 插件列表

```bash
jeecf plugin
```

2. 插件支持的语言列表

```bash
jeecf plugin --language
```

3. 插件详情
```bash
jeecf plugin <name>
```

### field

1. 属性列表
```bash
jeecf field
```

2. 属性详情
```bash
jeecf field <name>
```

### template

1. 模板列表
```bash
jeecf template
```

2. 拉取模板
```bash
jeecf template pull <name>
```
