# jeecf-cli

![](https://img.shields.io/pypi/v/jeecf.svg)

## Introduce

Command line toolbox of [Jeecf](https://github.com/cgfly/jeecf)

## Install

> pip install jeecf

## Commands

### 1. login

```bash
jeecf login <url>
```

### 2. namespace

1. 获取命名空间列表并标出当前命名空间

```bash
jeecf namespace
```

2. 切换命名空间

```bash
jeecf namespace use <name>
```

### 3. dbsource

1. 获取数据源列表并标出当前数据源

```bash
jeecf dbsource
```

2. 切换数据源

```bash
jeecf dbsource use <name>
```

### 4. plugin

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

### 5. field

1. 属性列表
```bash
jeecf field
```

2. 属性详情
```bash
jeecf field <name>
```

### 6. template

1. 模板列表
```bash
jeecf template
```

2. 拉取模板
```bash
jeecf template pull <name>
```

3. 根据模板生成代码
```bash
jeecf template gen xxx.yml
```

4. 上传模板
```bash
jeecf template push xxx.zip
```
