redirect() is used to redirect views to another view

`return redirect("book_read")`

to update instance in form
form = BookForm(request.POST, instance=book)


to upload file from post
<form method='post' action='' class='main' enctype='multipart/form-data'>