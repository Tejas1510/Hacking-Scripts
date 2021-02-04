package github.com.st235.easycurrency.data.net

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

typealias RatesMap = MutableMap<String, Double>

data class CurrencyRateResponse(@SerializedName("base") @Expose val base: String,
                                @SerializedName("date") @Expose val date: String,
                                @SerializedName("rates") @Expose val rates: RatesMap) {
    companion object {
        fun createWithTimestamp(base: String, date: String,
                                rates: RatesMap, timestamp: Long): CurrencyRateResponse {
            val response = CurrencyRateResponse(base, date, rates)
            response.unixTimestamp = timestamp
            return response
        }
    }

    var unixTimestamp: Long = 0L
}
