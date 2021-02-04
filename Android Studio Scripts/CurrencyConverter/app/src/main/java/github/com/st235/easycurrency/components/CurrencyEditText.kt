package github.com.st235.easycurrency.components

import android.content.Context
import android.graphics.Canvas
import android.graphics.Paint
import android.text.TextWatcher
import android.text.method.DigitsKeyListener
import android.util.AttributeSet
import android.view.Gravity
import android.view.LayoutInflater
import android.view.View
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import androidx.core.content.ContextCompat
import github.com.st235.easycurrency.R
import github.com.st235.easycurrency.utils.CurrencyUtils
import github.com.st235.easycurrency.utils.extensions.toPx

/**
 * Input field which contains hint field with
 * currency sign label
 */
class CurrencyEditText @JvmOverloads constructor(
        context: Context, attrs: AttributeSet? = null, defStyleAttr: Int = 0)
    : LinearLayout(context, attrs, defStyleAttr) {
    companion object {
        private val UNDERLINE_WIDTH = 1F.toPx()
    }

    private val paint = Paint(Paint.ANTI_ALIAS_FLAG)

    private val inputEt: EditText
    private val signTv: TextView

    init {
        setWillNotDraw(false)
        orientation = LinearLayout.HORIZONTAL
        gravity = Gravity.CENTER_VERTICAL
        isClickable = true
        isFocusable = true
        isFocusableInTouchMode = true

        val underlineColor = ContextCompat.getColor(context, R.color.colorCurrencyInputUnderline)
        paint.style = Paint.Style.FILL
        paint.color = underlineColor
        paint.strokeWidth = UNDERLINE_WIDTH

        val v = LayoutInflater.from(getContext()).inflate(R.layout.content_currency_edittext, this)
        inputEt = v.findViewById(R.id.input)
        signTv = v.findViewById(R.id.sign)

        inputEt.hint = CurrencyUtils.getCurrencyInputPlaceholder()
        inputEt.keyListener = DigitsKeyListener.getInstance(CurrencyUtils.getCurrencyAllowedSymbols())

        inputEt.onFocusChangeListener = View.OnFocusChangeListener { iv, f ->
            onFocusChangeListener.onFocusChange(iv, f)
        }
    }

    override fun onDraw(canvas: Canvas?) {
        super.onDraw(canvas)
        val height = height.toFloat()
        val width = width.toFloat()
        canvas?.drawLine(0F, height, width, height, paint)
    }

    fun addTextWatcher(textWatcher: TextWatcher) {
        inputEt.addTextChangedListener(textWatcher)
    }

    fun removeTextWatcher(textWatcher: TextWatcher) {
        inputEt.removeTextChangedListener(textWatcher)
    }

    fun changeInputText(charSequence: CharSequence) {
        inputEt.setText(charSequence)
    }

    fun setSign(sign: CharSequence) {
        signTv.text = sign
    }
}
