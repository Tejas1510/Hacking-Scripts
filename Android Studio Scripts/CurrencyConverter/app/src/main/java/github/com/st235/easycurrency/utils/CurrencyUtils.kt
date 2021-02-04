package github.com.st235.easycurrency.utils

import java.text.DecimalFormatSymbols
import java.util.*

/**
 * Helps to work with currencies
 * and predefined local preferences
 */
object CurrencyUtils {
    private const val ASCII_OFFSET = 0x41
    private const val UNICODE_FLAG_OFFSET = 0x1F1E6
    private const val CURRENCY_PLACEHOLDER_MASK = "0%s00"
    private const val CURRENCY_OUTPUT_MASK = "%.2f"

    private val decimalFormatSymbols = DecimalFormatSymbols.getInstance()

    private var currencyInputPlaceholder: String? = null
    private var currencyDecimalAllowedSymbols: String? = null

    /**
     * @return currency localized title by ISO 4217 code
     */
    fun getCurrencyTitleBy(code: String) = Currency.getInstance(code).displayName

    /**
     * @return currency currency special sign by ISO 4217 code
     */
    fun getCurrencySignBy(code: String) = Currency.getInstance(code).symbol

    /**
     * PS: not all of the vendors put in flags emoji
     * at build-in font, so, we should use our one
     * @return currency emoji symbol by ISO 4217 code
     */
    fun getCurrencyFlagEmojiBy(code: String): String {
        val firstChar = Character.codePointAt(code, 0) - ASCII_OFFSET + UNICODE_FLAG_OFFSET
        val secondChar = Character.codePointAt(code, 1) - ASCII_OFFSET + UNICODE_FLAG_OFFSET
        return String(Character.toChars(firstChar)) + String(Character.toChars(secondChar))
    }

    /**
     * @return converted value of passed currency in terms of base currency
     */
    fun calculateBaseValue(newValue: Double,
                           currency: github.com.st235.easycurrency.domain.Currency) =
            newValue / currency.rate

    /**
     * @return symbols that user should use to write at input field, including
     * local aligned decimal signs separator
     */
    fun getCurrencyAllowedSymbols(): String {
        if (currencyDecimalAllowedSymbols == null) {
            val separator = decimalFormatSymbols.decimalSeparator
            currencyDecimalAllowedSymbols = "0123456789$separator"
        }

        return currencyDecimalAllowedSymbols!!
    }

    /**
     * @return currency decimal separator for current locale
     */
    fun getCurrencySeparator() = decimalFormatSymbols.decimalSeparator

    /**
     * @return text placeholder separated by local sign
     */
    fun getCurrencyInputPlaceholder(): String {
        if (currencyInputPlaceholder == null) {
            val separator = decimalFormatSymbols.decimalSeparator
            currencyInputPlaceholder = CURRENCY_PLACEHOLDER_MASK.format(separator)
        }

        return currencyInputPlaceholder!!
    }

    /**
     * @return formats current input by predefined mask [CURRENCY_OUTPUT_MASK]
     */
    fun getCurrencyOutputText(value: Double) = CURRENCY_OUTPUT_MASK.format(value)
}
