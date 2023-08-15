from web import create_app, siwa

app = create_app()


# celery_app = app.extensions['celery']


@app.route('/', methods=['GET'])
@siwa.doc()
def hello_world():  # put application's code here
    return 'Hello World!'


# @scheduler.task('interval', id='do_job_1', seconds=5)  # 循环任务，每5秒循环一次
# def job1():
#     pass


if __name__ == '__main__':
    app.run()
