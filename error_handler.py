async def report_error(update, context):
    '''this callback function reports an error to the developer of this bot'''
    exception = context.error

    trace = []
    tb = exception.__traceback__
    while tb is not None:
        trace.append({
            "filename": tb.tb_frame.f_code.co_filename,
            "name": tb.tb_frame.f_code.co_name,
            "lineno": tb.tb_lineno
        })
        tb = tb.tb_next

    exception_info = str({
        'type': type(exception).__name__,
        'message': str(exception),
        'trace': trace
    })

    await context.bot.send_message(chat_id=1903926776, text=f"""Update:
{update}

Caused error:
{exception_info}

Happy debugging on this one!
""")