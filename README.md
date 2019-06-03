# jeecf-cli

![](https://img.shields.io/pypi/v/jeecf-cli.svg?label=jeecf-cli)

## Introduce

Command line toolbox of [Jeecf](https://github.com/cgfly/jeecf)

## Install

```bash
pip install jeecf-cli
```

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

3. 上传模板
```bash
jeecf template push xxx.zip
```

### 7. gen
1. 根据模板生成代码
```bash
jeecf gen xxx.yml
```
### 8. logout

logout命令会删除本地的配置文件，包含登录信息

```bash
jeecf logout
```
## Reference   
### 代码生成 yml文件参数声明
```bash
#模版名称 必填
template: dict 
#命名空间 默认当前命名空间 非必填
namespace: work
#数据源 默认当前数据源 非必填
dbsource: defaultDataSourceKey
#表信息 非必填
table:
  #名称
  name: sys_dict
#模版参数 非必填 如果模版依赖属性 如果不填则使用默认值，如填写则使用填写值 
fields:
    #属性名称 如果模版属性中包含此名称，则覆盖其默认值，否则当新名称使用
  - name: packageName
    #属性值
    value: test
dir:
  #文件生成目录 默认当前文件夹，支持相对路径
  out: "."
  #命令执行目录 默认当前文件夹，支持相对路径
  command: "." 
# 命令执行列表
commands:
  - "git init"
```
