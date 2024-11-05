# esports
电竞赛事api开发

# esports API README

## 1. 项目概述
本项目是一个电竞赛事相关的API开发项目，主要提供了与电竞赛事、战队、图片处理等相关的接口。

## 2. 项目结构
- `api/v1/`目录下包含了各个模块的API接口实现，如`imageprocess`、`match`、`team`、`tournament`等。
- `middleware`目录包含了中间件相关的代码，用于处理如缓存、认证、预测结算等功能。
- `spider`目录可能包含了用于爬取数据的相关代码（从部分代码逻辑推测）。
- `utils`目录包含了一些工具函数和初始化配置、数据库连接等相关代码。

## 3. 路由设置
### 3.1 总体路由设置
`Router`函数是整个项目的路由设置核心函数，它创建了一个`gin.Engine`实例，并进行了一系列的配置和路由注册。
1. **CORS中间件配置**
   - 允许来自`http://localhost:5173`的跨域请求，允许的方法包括`GET`、`POST`、`PUT`、`DELETE`、`OPTIONS`，允许的头部包括`Origin`、`Content-Type`、`Accept`、`Authorization`，并且允许携带凭证。
2. **配置文件和数据库初始化**
   - 调用`utils.InitConfig`和`utils.InitRedis`进行配置文件读取和Redis数据库初始化。同时创建了`redisClient`和`sqlClient`分别用于操作Redis和数据库（从代码推测可能是关系型数据库，但具体类型未明确）。
3. **缓存中间件配置**
   - 创建了`cacheMiddleware`并应用到整个引擎。在缓存更新期间，通过`lock`锁来控制并发访问，并且可以通过`skipCacheDuringUpdate`变量来决定是否跳过缓存处理。
4. **定时任务设置**
   - 创建了`gocron`定时任务调度器，每20秒执行一次缓存更新任务。缓存更新任务中，先设置`skipCacheDuringUpdate`为`true`，然后调用`cache.UpdateAllCache`更新缓存，最后再设置`skipCacheDuringUpdate`为`false`。
   - 同时创建了一个`time.NewTicker`定时器，每小时执行一次`spider.Transcation`函数（具体功能可能是数据爬取和事务处理相关，需查看`spider`模块代码）。
   - 还模拟了一个每5秒执行一次`settleFunc`（用于结算预测，具体功能需查看`middleware`模块代码）的定时器。
5. **Swagger文档和静态资源配置**
   - 通过`setupSwagger`函数添加了Swagger路由，通过`setupStaticFiles`函数设置了静态资源目录`/resource`。

### 3.2 各个模块路由
1. **图片处理路由（`imageprocess`）**
   - 路由前缀为`/api/v1/imageprocess`，提供了`GetImages`接口，用于获取图片相关信息（具体功能需查看`imageprocess.GetImages`函数实现）。
2. **赛事路由（`match`）**
   - 路由前缀为`/api/v1/match/`，提供了多个接口，如`GetRaceCalendarList`、`GetRaceCalendarListByTitle`等，用于获取赛事日程相关信息（具体功能需查看`match`模块中各个函数实现）。
3. **战队路由（`team`）**
   - 路由前缀为`/api/v1/team/`，提供了`GetLegacyList`、`GetPlayerAndTeamDataByTeam`等接口，用于获取战队相关信息（具体功能需查看`team`模块中各个函数实现）。
4. **赛事信息路由（`tournament`）**
   - 路由前缀为`/api/v1/tournament/`，提供了`GetTournaments`、`GetWeiboData`等接口，用于获取赛事相关的微博数据、文章数据等信息（具体功能需查看`tournament`模块中各个函数实现）。

## 4. 如何运行
1. 确保已经安装了项目所需的依赖，如`gin`、`gocron`、`swaggo`等相关库。
2. 配置好`utils`模块中所需的配置文件，包括Redis连接配置和可能的数据库连接配置等。
3. 运行项目的入口文件（如果有的话，从提供的代码中未明确），项目将启动并监听相应的端口（未明确具体端口，但可以推测如果是本地开发，可能是默认的`gin`端口或者通过配置文件指定的端口）。

## 5. 接口文档
项目中集成了Swagger文档，可以通过访问`/swagger/*any`路径查看接口文档，了解各个接口的详细参数和返回值信息。