# AutoHosts
个人用，自动更新Hosts的脚本，仅供学习使用。

目前已经添加了GitHub和Coursera。

## 使用

> 注意：需要python和pip环境

### Clone到本地

```bash
git clone https://github.com/zzxzzk115/AutoHosts.git
```

### 安装依赖

Linux:

```bash
cd AutoHosts
./install_dependencies.sh
```

Windows:

双击运行`install_dependencies.bat`

### 运行

在`AutoHosts`中打开终端或者cmd：

```bash
python main.py
```

### 自定义插件

在`AutoHosts/plugins`中添加`plugin_xxx.py`，详细方法请参考`AutoHosts/plugins/`中的源码。

