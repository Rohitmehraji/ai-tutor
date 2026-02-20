import { useMemo, useState } from 'react'

const languageOptions = [
  { code: 'en', label: 'English' },
  { code: 'hi', label: 'हिन्दी (Hindi)' },
  { code: 'ta', label: 'தமிழ் (Tamil)' },
  { code: 'bn', label: 'বাংলা (Bengali)' },
  { code: 'te', label: 'తెలుగు (Telugu)' },
  { code: 'mr', label: 'मराठी (Marathi)' },
]

const ageBands = ['1-5', '6-12', '13-18', '19-35', '36-60', '60+']

const translation = {
  en: {
    heading: 'Build confident learners in every language.',
    subheading:
      'Ultra-modern AI tutor workspace with adaptive pathways, voice-first accessibility, and context-rich explanations for every age group.',
    cta: 'Start personalized session',
    detect: 'Auto-detect learner language',
    featureTitle: 'AI engine capabilities',
    recommend: 'Recommended next focus',
  },
  hi: {
    heading: 'हर भाषा में आत्मविश्वासी शिक्षार्थी तैयार करें।',
    subheading:
      'अत्याधुनिक AI ट्यूटर अनुभव: अनुकूली सीखने के मार्ग, वॉइस-फर्स्ट एक्सेसिबिलिटी और हर आयु के लिए संदर्भपूर्ण समझ।',
    cta: 'व्यक्तिगत सत्र शुरू करें',
    detect: 'सीखने वाले की भाषा स्वतः पहचानें',
    featureTitle: 'AI इंजन की क्षमताएँ',
    recommend: 'अगला सुझाया गया फोकस',
  },
  ta: {
    heading: 'ஒவ்வொரு மொழியிலும் நம்பிக்கையுடன் கற்றலை உருவாக்குங்கள்.',
    subheading:
      'அல்ட்ரா-மாடர்ன் AI டியூட்டர்: வயதுக்கு ஏற்ற தனிப்பயன் கற்றல், குரல் ஆதரவு மற்றும் சூழல் விளக்கங்களுடன்.',
    cta: 'தனிப்பயன் அமர்வை தொடங்கு',
    detect: 'கற்றுநரின் மொழியை தானாக கண்டறி',
    featureTitle: 'AI இயந்திர திறன்கள்',
    recommend: 'அடுத்த பரிந்துரைக்கப்பட்ட கவனம்',
  },
}

const coreFeatures = [
  'Real-time multilingual tutoring with translation controls',
  'Adaptive pathways based on speed, confidence, and accuracy',
  'Voice interaction (speech-to-text and text-to-speech)',
  'Personalized recommendations from learning history',
  'Gamification with levels, streaks, and achievements',
  'Live AI doubt solver with contextual explanations',
  'Teacher/parent analytics for progress and risk alerts',
]

const journeyStages = [
  { title: 'Discover', detail: 'Select age, goals, and preferred language in one guided flow.' },
  { title: 'Learn', detail: 'Concept cards, quizzes, stories, and voice tutoring adapt in real time.' },
  { title: 'Master', detail: 'Earn badges, level up, and unlock challenge-based pathways.' },
]

export default function App() {
  const [language, setLanguage] = useState('en')
  const [selectedAge, setSelectedAge] = useState('6-12')
  const [autoDetect, setAutoDetect] = useState(true)
  const [checkedNeeds, setCheckedNeeds] = useState({
    dyslexiaSupport: false,
    lowVision: false,
    voiceOnly: true,
    parentInsights: true,
  })

  const copy = translation[language] || translation.en

  const activeRoadmap = useMemo(
    () => [
      `Age band: ${selectedAge}`,
      autoDetect ? 'Language detection enabled' : 'Manual language mode',
      checkedNeeds.voiceOnly ? 'Voice-first lesson mode ready' : 'Voice support optional',
      checkedNeeds.parentInsights ? 'Parent/teacher analytics enabled' : 'Analytics available on demand',
    ],
    [selectedAge, autoDetect, checkedNeeds]
  )

  const toggleNeed = (key) => {
    setCheckedNeeds((prev) => ({ ...prev, [key]: !prev[key] }))
  }

  return (
    <main className="page">
      <header className="hero glass">
        <div>
          <p className="eyebrow">AI Tutor Engine • Personalized • Inclusive</p>
          <h1>{copy.heading}</h1>
          <p className="subtext">{copy.subheading}</p>
        </div>
        <button className="primaryBtn">{copy.cta}</button>
      </header>

      <section className="glass controls">
        <h2>Learner Experience Controls</h2>
        <div className="controlGrid">
          <label>
            Preferred Language
            <select value={language} onChange={(e) => setLanguage(e.target.value)}>
              {languageOptions.map((lang) => (
                <option value={lang.code} key={lang.code}>
                  {lang.label}
                </option>
              ))}
            </select>
          </label>

          <label>
            Age Group
            <select value={selectedAge} onChange={(e) => setSelectedAge(e.target.value)}>
              {ageBands.map((band) => (
                <option value={band} key={band}>
                  {band}
                </option>
              ))}
            </select>
          </label>
        </div>

        <label className="checkboxRow">
          <input type="checkbox" checked={autoDetect} onChange={() => setAutoDetect((v) => !v)} />
          {copy.detect}
        </label>

        <div className="needsGrid">
          <label className="checkboxRow">
            <input
              type="checkbox"
              checked={checkedNeeds.dyslexiaSupport}
              onChange={() => toggleNeed('dyslexiaSupport')}
            />
            Dyslexia-friendly typography
          </label>
          <label className="checkboxRow">
            <input type="checkbox" checked={checkedNeeds.lowVision} onChange={() => toggleNeed('lowVision')} />
            High contrast mode
          </label>
          <label className="checkboxRow">
            <input type="checkbox" checked={checkedNeeds.voiceOnly} onChange={() => toggleNeed('voiceOnly')} />
            Voice-first learning journey
          </label>
          <label className="checkboxRow">
            <input
              type="checkbox"
              checked={checkedNeeds.parentInsights}
              onChange={() => toggleNeed('parentInsights')}
            />
            Parent/teacher progress insights
          </label>
        </div>
      </section>

      <section className="gridTwo">
        <article className="glass">
          <h2>{copy.featureTitle}</h2>
          <ul>
            {coreFeatures.map((feature) => (
              <li key={feature}>{feature}</li>
            ))}
          </ul>
        </article>

        <article className="glass">
          <h2>{copy.recommend}</h2>
          <div className="recommendation">Interactive storytelling + visual quiz loop for {selectedAge} learners.</div>
          <ul>
            {activeRoadmap.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </article>
      </section>

      <section className="glass">
        <h2>Adaptive Learning Journey</h2>
        <div className="journey">
          {journeyStages.map((stage) => (
            <article key={stage.title} className="journeyCard">
              <h3>{stage.title}</h3>
              <p>{stage.detail}</p>
            </article>
          ))}
        </div>
      </section>
    </main>
  )
}
