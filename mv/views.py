from django.shortcuts import render, redirect
from .models import MusicVideo, Review
from .serializers import ReviewSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.


def mv_list(request):

    videos = MusicVideo.objects.all()

    return render(request, 'mvList.html', {'videos': videos})


def mv_detail(request, id):
    try:
        video = MusicVideo.objects.get(pk=id)
        return render(request, 'mvDetail.html', {'video': video})
    except MusicVideo.DoesNotExist:
        return redirect('/404')


def create_review(request, mv_id):
    try:
        video = MusicVideo.objects.get(pk=mv_id)

        review = Review()
        # 로그인 과정 없으니 아무 유저나 가져와서 입력
        review.author = User.objects.all().first()
        review.video = video
        review.text = request.POST["text"]
        review.score = request.POST["score"]

        review.save()
        return redirect('mv_detail', mv_id)
    except MusicVideo.DoesNotExist:
        print("해당 뮤직비디오가 존재하지 않음")
        return redirect('mv_detail', mv_id)


@api_view(['GET'])
def get_review_for_mv(request, mv_id):
    if request.method == 'GET':
        reviews = Review.objects.filter(video=mv_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
