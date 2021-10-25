from ninja_extra import APIController, route, router
from ninja_extra.permissions import AllowAny
from ninja_jwt import schema


class TokenVerificationController(APIController):
    @route.post('/verify-token', response=schema.TokenVerifySerializer)
    def verify_token(self, token: str):
        verified_token = schema.TokenVerifySerializer(token=token)
        return verified_token


class TokenBlackListController(APIController):
    @route.post('/blacklist-token', response=schema.TokenBlacklistSerializer)
    def blacklist_token(self, token: str):
        verified_token = schema.TokenVerifySerializer(token=token)
        return verified_token


class TokenObtainPairController(APIController):
    @route.post('/obtain-token', response=schema.TokenObtainPairOutput)
    def obtain_token(self, user: schema.TokenObtainPairSerializer):
        return user.output_schema()

    @route.post('/refresh-token', response=schema.TokenRefreshSerializer)
    def refresh_token(self, refresh_token: str):
        refresh_token = schema.TokenRefreshSerializer(refresh=refresh_token)
        return refresh_token


class TokenObtainSlidingController(TokenObtainPairController):
    @route.post('/obtain-token', response=schema.TokenObtainSlidingOutput)
    def obtain_token(self, user: schema.TokenObtainSlidingSerializer):
        return user.output_schema()

    @route.post('/refresh-token', response=schema.TokenRefreshSlidingSerializer)
    def refresh_token(self, refresh_token: str):
        refresh_token = schema.TokenRefreshSlidingSerializer(token=refresh_token)
        return refresh_token


@router('/api', permissions=[AllowAny], tags=['token'])
class SimpleJWTDefaultController(TokenVerificationController, TokenObtainPairController):
    """SimpleJWT Default controller for obtaining and refreshing tokens"""
    pass
