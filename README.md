```

# 创建项目
django-admin startproject manyueol

# 创建应用
django-admin startapp captcha_test




# create migrations for those changes
python manage.py makemigrations polls

# apply those changes to the database//初始化数据库
python manager.py migrate

# 显示Migrate的SQL
python manage.py sqlmigrate polls 0001

# 运行项目
python manager.py runserver

```

```

# 运行交互模式
python manager.py shell

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
Question.objects.all()
c = q.choice_set.all()
q.choice_set.create(choice_text='Just hacking again', votes=0)


```

```
python manage.py createsuperuser

```

