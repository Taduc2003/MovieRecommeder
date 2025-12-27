from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth import get_user_model
from movies.models import Movie
from .models import Suggestion


@require_GET
def api_suggestions(request):
    """
    Retrieve movie suggestions for a specific user.

    This API endpoint fetches personalized movie recommendations for a user based on:
    1. Suggestions ranked by 'value' (relevance score from the recommendation model)
    2. Movies filtered to only include those the user hasn't rated yet (did_rate=False)
    3. Final results sorted by 'score' (movie's popularity/rating score)
    4. Limited to top 50 movies

    Args:
        request (HttpRequest): HTTP request containing 'user_id' as GET parameter

    Returns:
        JsonResponse: JSON response containing:
            - success: List of dicts with movie data (id, title, overview)
            - error cases: Error message with appropriate HTTP status code

    Raises:
        JsonResponse with status 400: If 'user_id' parameter is missing
        JsonResponse with status 404: If user with given user_id doesn't exist

    Note:
        - 'value': Recommendation score from Suggestion model (how relevant the suggestion is for this user)
        - 'score': Movie's own score/rating (how popular/highly-rated the movie itself is)
        The two are different: value = personalized relevance, score = movie's absolute quality
    """
    user_id = request.GET.get('user_id')
    if not user_id:
        return JsonResponse({'error': 'Missing user_id'}, status=400)
    try:
        user = get_user_model().objects.get(pk=user_id)
    except get_user_model().DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    suggestion_qs = Suggestion.objects.filter(user=user, did_rate=False)
    movie_ids = suggestion_qs.order_by(
        '-value').values_list('object_id', flat=True)
    movies = Movie.objects.filter(pk__in=movie_ids).order_by('-score')
    # Lấy tối đa 50 phim có score cao nhất
    movies = movies[:50]
    movie_list = []
    for m in movies:
        movie_list.append({
            'id': m.id,
            'title': m.title,
            'overview': m.overview if hasattr(m, 'overview') else '',
        })
    return JsonResponse({'suggestions': movie_list})
