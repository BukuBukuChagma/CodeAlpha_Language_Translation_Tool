// Language list for dropdowns
const languages = {
    'auto': 'Detect Language',
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'zh-cn': 'Chinese (Simplified)',
    'ar': 'Arabic',
    'hi': 'Hindi'
};

// DOM Elements
const sourceText = document.getElementById('sourceText');
const targetText = document.getElementById('targetText');
const sourceLanguage = document.getElementById('sourceLanguage');
const targetLanguage = document.getElementById('targetLanguage');
const translateBtn = document.getElementById('translateBtn');
const swapBtn = document.getElementById('swapLanguages');
const clearBtn = document.getElementById('clearSource');
const copyBtn = document.getElementById('copyTranslation');

// Populate language dropdowns
function populateLanguages() {
    for (const [code, name] of Object.entries(languages)) {
        if (code !== 'auto') {
            const sourceOption = new Option(name, code);
            const targetOption = new Option(name, code);
            sourceLanguage.add(sourceOption);
            targetLanguage.add(targetOption);
        }
    }
}

// Translation function
async function translateText() {
    const text = sourceText.value.trim();
    if (!text) return;

    translateBtn.disabled = true;
    try {
        const response = await fetch('/api/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                source_lang: sourceLanguage.value,
                target_lang: targetLanguage.value
            })
        });

        const data = await response.json();
        if (response.ok) {
            targetText.value = data.translated_text;
        } else {
            throw new Error(data.error || 'Translation failed');
        }
    } catch (error) {
        alert('Translation error: ' + error.message);
        targetText.value = '';
    } finally {
        translateBtn.disabled = false;
    }
}

// Language detection function
async function detectLanguage(text) {
    if (!text.trim()) return;
    
    try {
        const response = await fetch('/api/detect', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();
        if (response.ok && data.detected_language) {
            sourceLanguage.value = data.detected_language;
        }
    } catch (error) {
        console.error('Language detection error:', error);
    }
}

// Event Listeners
translateBtn.addEventListener('click', translateText);

sourceText.addEventListener('input', () => {
    if (sourceLanguage.value === 'auto') {
        const debounceTimer = setTimeout(() => {
            detectLanguage(sourceText.value);
        }, 500);
        return () => clearTimeout(debounceTimer);
    }
});

swapBtn.addEventListener('click', () => {
    if (sourceLanguage.value === 'auto') return;
    
    const tempLang = sourceLanguage.value;
    const tempText = sourceText.value;
    
    sourceLanguage.value = targetLanguage.value;
    sourceText.value = targetText.value;
    
    targetLanguage.value = tempLang;
    targetText.value = tempText;
});

clearBtn.addEventListener('click', () => {
    sourceText.value = '';
    targetText.value = '';
    sourceText.focus();
});

copyBtn.addEventListener('click', async () => {
    if (!targetText.value) return;
    
    try {
        await navigator.clipboard.writeText(targetText.value);
        const originalText = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="fas fa-check"></i>';
        setTimeout(() => {
            copyBtn.innerHTML = originalText;
        }, 2000);
    } catch (err) {
        console.error('Failed to copy text:', err);
    }
});

// Initialize
populateLanguages();
