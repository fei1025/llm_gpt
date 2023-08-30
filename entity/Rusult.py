def success_response(data=None, message="操作成功"):
    return {
        "status": "success",
        "message": message,
        "data": data
    }


def error_response(message="操作失败"):
    return {
        "status": "error",
        "message": message
    }
