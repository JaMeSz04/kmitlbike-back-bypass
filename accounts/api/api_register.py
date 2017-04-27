def register(request):
    if request.method == "POST":
        try:
            user_form = UserValidationForm(request.POST).get_cleaned_data()
            username = user_form["username"]
            first_name = user_form["first_name"]
            last_name = user_form["last_name"]
            email = user_form["email"]
            gender = user_form["gender"]
            phone_no = user_form["phone_no"]

            try:
                user = User.objects.create_user(username=username,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email)
                UserProfile.objects.create(user=user, gender=gender, phone_no=phone_no)
                try:
                    User.objects.get(username=username)
                    return HttpResponse(status=HTTP_201_CREATED, content_type="application/json")
                except User.DoesNotExist:
                    response = {"message": "Fail to create new user. Please try again later."}
                    return HttpResponse(json.dumps(response), status=HTTP_406_NOT_ACCEPTABLE,
                                        content_type="application/json")
            except IntegrityError:
                response = {"message": "This user already exists"}
                return HttpResponse(json.dumps(response), status=HTTP_406_NOT_ACCEPTABLE,
                                    content_type="application/json")
        except ValidationError as e:
            response = {"message": str(e.message)}
            return HttpResponse(json.dumps(response), status=HTTP_406_NOT_ACCEPTABLE, content_type="application/json")
    else:
        return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")