Online-questionnaire-survey-system
==================================


[**WIP， Please review**]
## 初始化工作空间及部署

1. 在合适的位置创建工作目录

2. 在目录内运行

        git clone git@github.com:BuaaBoys/Online-questionnaire-survey-system.git

3. 在qsystem目录下运行

        python manage.py syncdb

4. 运行

        python manage.py runserver

5. 打开浏览器访问[localhost:8000](http://localhost:8000)

## 工作流

1. 更新本地master到最新：

        git pull origin master

2. 为当前用户故事创建一个本地分支：

        git branch story-42
        git checkout story-42

3. 在新分支上开发并add、commit：

        //hackhackhack...
        //git add ...
        //git commit [-m] ...

4. 合并该分支之前若在开发过程中如果origin/master存在更新，先更新本地master及故事分支，解决冲突并通过测试后再push：

        git checkout master
        git pull origin master
        git checkout story-42
        git rebase master
        //解决冲突
        git checkout master
        git merge story-42
        git push origin master

5. 删除本地分支：

        git branch -d story-42

## 其他流程

可自行选择是否将story分支push到origin repo以作备份只用，但请及时清理过期的分支。

* 创建远程分支：

        git push origin story-42:story-42
        
* 更新远程分支：

        git push origin story-42
        
* 删除远程分支：

        git push origin :story-42
        
* 获取不在本地的远程分支：

        git fetch
        git checkout -b local-story-24 origin/remote-story-24
        
