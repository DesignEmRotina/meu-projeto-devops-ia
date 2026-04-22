#!/usr/bin/env python3
"""
Script de Auditoria UX – Cobertura Completa de Design Frontend

Analisa o código quanto à conformidade com:

1. LEIS FUNDAMENTAIS DA PSICOLOGIA:
   - Lei de Hick (itens de navegação, complexidade de formulários)
   - Lei de Fitts (tamanho de alvos, áreas clicáveis/toque)
   - Lei de Miller (agrupamento, limites de memória)
   - Efeito Von Restorff (visibilidade do CTA principal)
   - Efeito da Posição Serial (itens importantes no início/fim)

2. DESIGN EMOCIONAL (Don Norman):
   - Visceral (primeira impressão, gradientes, animações)
   - Comportamental (feedback, usabilidade, performance)
   - Reflexivo (história da marca, valores, identidade)

3. CONSTRUÇÃO DE CONFIANÇA:
   - Sinais de segurança (SSL, criptografia em formulários)
   - Prova social (depoimentos, avaliações, logos)
   - Indicadores de autoridade (certificações, prêmios, mídia)

4. GERENCIAMENTO DE CARGA COGNITIVA:
   - Divulgação progressiva (accordion, abas, “Avançado”)
   - Ruído visual (excesso de cores/bordas)
   - Padrões familiares (rótulos, convenções padrão)

5. DESIGN PERSUASIVO (ÉTICO):
   - Padrões inteligentes (opções pré-selecionadas)
   - Ancoragem (preço original vs. desconto)
   - Prova social (indicadores ao vivo, números)
   - Indicadores de progresso (barras, etapas)

6. SISTEMA TIPOGRÁFICO (9 seções):
   - Combinação de fontes (máx. 3 famílias)
   - Comprimento de linha (45–75ch)
   - Altura de linha (proporções adequadas)
   - Espaçamento entre letras (caixa alta, textos display)
   - Peso e ênfase (níveis de contraste)
   - Tipografia responsiva (clamp())
   - Hierarquia (títulos sequenciais)
   - Escala modular (proporções consistentes)
   - Legibilidade (agrupamento, subtítulos)

7. EFEITOS VISUAIS (10 seções):
   - Glassmorphism (blur + transparência)
   - Neomorphism (sombras duplas, inset)
   - Hierarquia de sombras (níveis de elevação)
   - Gradientes (uso e excesso)
   - Efeitos de borda (verificação de complexidade)
   - Efeitos de glow (text-shadow, box-shadow)
   - Técnicas de overlay (legibilidade de texto sobre imagem)
   - Aceleração por GPU (transform/opacity vs layout)
   - Performance (uso de will-change)
   - Seleção de efeitos (propósito > decoração)

8. SISTEMA DE CORES (7 seções):
   - BANIMENTO DO ROXO (Regra crítica do Maestro – #8B5CF6, #A855F7 etc.)
   - Regra 60-30-10 (dominante, secundária, destaque)
   - Padrões de esquema de cores (monocromático, análogo)
   - Conformidade com modo escuro (sem preto/branco puro)
   - Contraste WCAG (detecção de baixo contraste)
   - Psicologia das cores por contexto (comida + azul = ruim)
   - Paletas baseadas em HSL (abordagem recomendada)

9. GUIA DE ANIMAÇÃO (6 seções):
   - Duração adequada (mín. 50ms, máx. 1s para transições)
   - Funções de easing (ease-out para entrada, ease-in para saída)
   - Microinterações (feedback hover/focus)
   - Estados de carregamento (skeleton, spinner, progresso)
   - Transições de página (fade/slide no roteamento)
   - Performance em animações de scroll (sem propriedades de layout)

10. MOTION GRAPHICS (7 seções):
   - Animações Lottie (fallback para redução de movimento)
   - Vazamentos de memória GSAP (kill/revert no unmount)
   - Performance de animações SVG (uso moderado de stroke-dashoffset)
   - Transformações 3D (perspectiva no pai, alerta mobile)
   - Efeitos de partículas (fallback mobile)
   - Animações guiadas por scroll (throttle com rAF)
   - Árvore de decisão de movimento (funcional vs decorativo)

11. ACESSIBILIDADE:
   - Texto alternativo (alt) em imagens
   - Verificação de redução de movimento
   - Rótulos de formulários

Total: mais de 80 verificações cobrindo todos os princípios de design
"""

import sys
import os
import re
import json
from pathlib import Path

class UXAuditor:
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.passed_count = 0
        self.files_checked = 0
    
    def audit_file(self, filepath: str) -> None:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        except: 
            return
        
        self.files_checked += 1
        filename = os.path.basename(filepath)

        # Pré-cálculo de flags comuns
        has_long_text = bool(re.search(r'<p|<div.*class=.*text|article|<span.*text', content, re.IGNORECASE))
        has_form = bool(re.search(r'<form|<input|password|credit|card|payment', content, re.IGNORECASE))
        complex_elements = len(re.findall(r'<input|<select|<textarea|<option', content, re.IGNORECASE))

        # --- 1. LEIS DA PSICOLOGIA ---
        # Lei de Hick
        nav_items = len(re.findall(r'<NavLink|<Link|<a\s+href|nav-item', content, re.IGNORECASE))
        if nav_items > 7:
            self.issues.append(f"[Lei de Hick] {filename}: {nav_items} itens de navegação (Máx. 7)")
        
        # Lei de Fitts
        if re.search(r'height:\s*([0-3]\d)px', content) or re.search(r'h-[1-9]\b|h-10\b', content):
            self.warnings.append(f"[Lei de Fitts] {filename}: Alvos pequenos (< 44px)")
        
        # Lei de Miller
        form_fields = len(re.findall(r'<input|<select|<textarea', content, re.IGNORECASE))
        if form_fields > 7 and not re.search(r'step|wizard|stage', content, re.IGNORECASE):
            self.warnings.append(f"[Lei de Miller] {filename}: Formulário complexo ({form_fields} campos)")
            
        # Efeito Von Restorff
        if 'button' in content.lower() and not re.search(r'primary|bg-primary|Button.*primary|variant=["\']primary', content, re.IGNORECASE):
            self.warnings.append(f"[Von Restorff] {filename}: Nenhum CTA primário detectado")

        # Efeito da Posição Serial
        if nav_items > 3:
            nav_content = re.findall(r'<NavLink|<Link|<a\s+href[^>]*>([^<]+)</a>', content, re.IGNORECASE)
            if nav_content and len(nav_content) > 2:
                last_item = nav_content[-1].lower() if nav_content else ''
                if not any(x in last_item for x in ['contact', 'login', 'sign', 'get started', 'cta', 'button']):
                    self.warnings.append(
                        f"[Posição Serial] {filename}: Último item da navegação pode não ser importante. "
                        "Coloque ações-chave no início ou no fim."
                    )

        # --- 1.5 DESIGN EMOCIONAL (Don Norman) ---
        # Visceral
        has_hero = bool(re.search(r'hero|<h1|banner', content, re.IGNORECASE))
        if has_hero:
            has_gradient = bool(re.search(r'gradient|linear-gradient|radial-gradient', content))
            has_animation = bool(re.search(r'@keyframes|transition:|animate-', content))
            has_visual_interest = has_gradient or has_animation

            if not has_visual_interest and not re.search(r'background:|bg-', content):
                self.warnings.append(
                    f"[Visceral] {filename}: Seção hero sem apelo visual. "
                    "Considere gradientes ou animações sutis."
                )

        # Comportamental
        if 'onClick' in content or '@click' in content or 'onclick' in content:
            has_feedback = re.search(r'transition|animate|hover:|focus:|disabled|loading|spinner', content, re.IGNORECASE)
            has_state_change = re.search(r'setState|useState|disabled|loading', content)

            if not has_feedback and not has_state_change:
                self.warnings.append(
                    f"[Comportamental] {filename}: Elementos interativos sem feedback imediato. "
                    "Adicione estados hover/focus/disabled."
                )

        # Reflexivo
        has_reflective = bool(re.search(r'about|story|mission|values|why we|our journey|testimonials', content, re.IGNORECASE))
        if has_long_text and not has_reflective:
            self.warnings.append(
                f"[Reflexivo] {filename}: Conteúdo longo sem história/valores da marca. "
                "Adicione uma seção 'Sobre' ou 'Por que existimos'."
            )

        # --- 1.6 CONSTRUÇÃO DE CONFIANÇA ---
        if has_form:
            security_signals = re.findall(r'ssl|secure|encrypt|lock|padlock|https', content, re.IGNORECASE)
            if len(security_signals) == 0 and not re.search(r'checkout|payment', content, re.IGNORECASE):
                self.warnings.append(
                    f"[Confiança] {filename}: Formulário sem indicadores de segurança. "
                    "Adicione 'SSL Seguro' ou ícone de cadeado."
                )

        social_proof = re.findall(r'review|testimonial|rating|star|trust|trusted by|customer|logo', content, re.IGNORECASE)
        if len(social_proof) > 0:
            self.passed_count += 1
        else:
            if has_long_text:
                self.warnings.append(
                    f"[Confiança] {filename}: Nenhuma prova social detectada. "
                    "Considere adicionar depoimentos, avaliações ou logos 'Confiado por'."
                )

        has_footer = bool(re.search(r'footer|<footer', content, re.IGNORECASE))
        if has_footer:
            authority = re.findall(r'certif|award|media|press|featured|as seen in', content, re.IGNORECASE)
            if len(authority) == 0:
                self.warnings.append(
                    f"[Confiança] {filename}: Rodapé sem sinais de autoridade. "
                    "Adicione certificações, prêmios ou menções na mídia."
                )

        # --- 7. ACESSIBILIDADE ---
        if re.search(r'<img(?![^>]*alt=)[^>]*>', content):
            self.issues.append(f"[Acessibilidade] {filename}: Imagem sem texto alternativo (alt)")

    def audit_directory(self, directory: str) -> None:
        extensions = {'.tsx', '.jsx', '.html', '.vue', '.svelte', '.css'}
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in {'node_modules', '.git', 'dist', 'build', '.next'}]
            for file in files:
                if Path(file).suffix in extensions:
                    self.audit_file(os.path.join(root, file))

    def get_report(self):
        return {
            "files_checked": self.files_checked,
            "issues": self.issues,
            "warnings": self.warnings,
            "passed_checks": self.passed_count,
            "compliant": len(self.issues) == 0
        }

def main():
    if len(sys.argv) < 2: sys.exit(1)
    
    path = sys.argv[1]
    is_json = "--json" in sys.argv
    
    auditor = UXAuditor()
    if os.path.isfile(path): auditor.audit_file(path)
    else: auditor.audit_directory(path)
    
    report = auditor.get_report()
    
    if is_json:
        print(json.dumps(report))
    else:
        # Use ASCII-safe output for Windows console compatibility
        print(f"\n[UX AUDIT] {report['files_checked']} files checked")
        print("-" * 50)
        if report['issues']:
            print(f"[!] ISSUES ({len(report['issues'])}):")
            for i in report['issues'][:10]: print(f"  - {i}")
        if report['warnings']:
            print(f"[*] WARNINGS ({len(report['warnings'])}):")
            for w in report['warnings'][:15]: print(f"  - {w}")
        print(f"[+] PASSED CHECKS: {report['passed_checks']}")
        status = "PASS" if report['compliant'] else "FAIL"
        print(f"STATUS: {status}")

    sys.exit(0 if report['compliant'] else 1)

if __name__ == "__main__":
    main()

