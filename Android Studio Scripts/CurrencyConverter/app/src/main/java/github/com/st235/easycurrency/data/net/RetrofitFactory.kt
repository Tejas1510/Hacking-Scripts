package github.com.st235.easycurrency.data.net

import com.google.gson.Gson
import com.google.gson.GsonBuilder
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitFactory {
    inline fun<reified T> createApiWrapper(baseUrl: String): T {
        val gson = GsonBuilder().excludeFieldsWithoutExposeAnnotation().create()
        val retrofit = Retrofit.Builder()
            .addConverterFactory(GsonConverterFactory.create(gson))
            .baseUrl(baseUrl)
            .build()

        return retrofit.create(T::class.java)
    }
}
