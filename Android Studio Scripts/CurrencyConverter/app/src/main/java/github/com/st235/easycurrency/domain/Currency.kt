package github.com.st235.easycurrency.domain

/**
 * Internal currency model, contains
 * id (ISO 4217 code), title (in local language)
 * current value, convert rate
 * and info about base value
 */
class Currency(val id: String,
               val title: String,
               var isBase: Boolean = false) {
    companion object {
        fun copy(currency: Currency, newRate: Double, newValue: Double): Currency {
            val newOne = Currency(currency)
            newOne.value = newValue
            newOne.rate = newRate
            return newOne
        }

        fun copyWithNewValue(currency: Currency, newValue: Double): Currency {
            val newOne = Currency(currency)
            newOne.value = newValue
            return newOne
        }
    }

    var value: Double = 1.0
    var rate: Double = 1.0

    constructor(currency: Currency): this(currency.id, currency.title, currency.isBase) {
        rate = currency.rate
    }

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (javaClass != other?.javaClass) return false

        other as Currency

        if (id != other.id) return false
        if (isBase != other.isBase) return false

        return true
    }

    override fun hashCode(): Int {
        var result = id.hashCode()
        result = 31 * result + isBase.hashCode()
        return result
    }

    override fun toString(): String {
        return "Currency(id='$id', title='$title', isBase=$isBase, value=$value, rate=$rate)"
    }
}
