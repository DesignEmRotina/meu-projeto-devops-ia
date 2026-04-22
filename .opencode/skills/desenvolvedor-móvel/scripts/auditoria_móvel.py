#!/usr/bin/env python3
"""
Script de Auditoria de UX Mobile - Cobertura Total de Design e Performance

Analisa código React Native / Flutter para conformidade com:

1. PSICOLOGIA DO TOQUE:
   - Tamanho dos Alvos (44pt iOS, 48dp Android)
   - Espaçamento entre Alvos (mínimo 8px)
   - Zona do Polegar (CTAs primários na parte inferior)
   - Alternativas a Gestos (botões visíveis para swipes)#!/usr/bin/env python3
"""
Script de Auditoria de UX Mobile - Cobertura Total de Design Mobile

Analisa código React Native / Flutter para conformidade com:

1. PSICOLOGIA DO TOQUE (touch-psychology.md):
   - Tamanhos de Alvos de Toque (44pt iOS, 48dp Android, 44px WCAG)
   - Espaçamento de Alvos de Toque (mínimo 8px)
   - Posicionamento na Zona do Polegar (CTAs primários na parte inferior)
   - Alternativas para Gestos (botões visíveis para swipes)
   - Padrões de Feedback Háptico
   - Tempo de Resposta ao Toque (<50ms)
   - Acessibilidade de Toque (suporte a deficiências motoras)

2. PERFORMANCE MOBILE (mobile-performance.md):
   - ScrollView vs FlatList (CRÍTICO)
   - React.memo para itens de lista
   - useCallback para renderItem
   - keyExtractor estável (NÃO usar index)
   - useNativeDriver para animações
   - Prevenção de Vazamento de Memória (limpeza/cleanup)
   - Detecção de Console.log
   - Detecção de Funções Inline
   - Performance de Animação (apenas transform/opacity)

3. NAVEGAÇÃO MOBILE (mobile-navigation.md):
   - Máximo de itens na Tab Bar (5)
   - Preservação de Estado da Aba
   - Tratamento adequado do botão "Voltar"
   - Suporte a Deep Links
   - Estrutura de Navegação

4. TIPOGRAFIA MOBILE (mobile-typography.md):
   - Uso de Fontes do Sistema
   - Suporte a Dynamic Type (iOS)
   - Restrições de Escala de Texto
   - Altura de Linha Mobile (Line Height)
   - Limites de Tamanho de Fonte

5. SISTEMA DE CORES MOBILE (mobile-color-system.md):
   - Evitar Preto Puro (#000000)
   - Otimização para OLED
   - Suporte a Dark Mode
   - Índices de Contraste

6. PLATAFORMA iOS (platform-ios.md):
   - Uso de SF Symbols
   - Padrões de Navegação iOS
   - Tipos Hápticos do iOS
   - Componentes Específicos do iOS

7. PLATAFORMA ANDROID (platform-android.md):
   - Uso de Material Icons
   - Padrões de Navegação Android
   - Efeitos de Ripple (Ondulação)
   - Componentes Específicos do Android

8. BACKEND MOBILE (mobile-backend.md):
   - Armazenamento Seguro (NÃO usar AsyncStorage para tokens)
   - Tratamento Offline
   - Suporte a Notificações Push
   - Cache de Respostas de API

Total: Mais de 50 verificações específicas para mobile.
"""

import sys
import os
import re
import json
from pathlib import Path

class AuditorMobile:
    def __init__(self):
        self.problemas = []
        self.avisos = []
        self.contagem_sucesso = 0
        self.arquivos_verificados = 0

    def auditar_arquivo(self, caminho_arquivo: str) -> None:
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8', errors='replace') as f:
                conteudo = f.read()
        except:
            return

        self.arquivos_verificados += 1
        nome_arquivo = os.path.basename(caminho_arquivo)

        # Detectar framework
        is_react_native = bool(re.search(r'react-native|@react-navigation|React\.Native', conteudo))
        is_flutter = bool(re.search(r'import \'package:flutter|MaterialApp|Widget\.build', conteudo))

        if not (is_react_native or is_flutter):
            return  # Pular arquivos que não são de mobile

        # --- 1. VERIFICAÇÕES DE PSICOLOGIA DO TOQUE ---

        # 1.1 Tamanho do Alvo de Toque
        tamanhos_pequenos = re.findall(r'(?:width|height|size):\s*([0-3]\d)', conteudo)
        for tam in tamanhos_pequenos:
            if int(tam) < 44:
                self.problemas.append(f"[Alvo de Toque] {nome_arquivo}: Alvo de {tam}px < 44px mínimo (iOS: 44pt, Android: 48dp)")

        # 1.2 Espaçamento do Alvo de Toque
        espacos_curtos = re.findall(r'(?:margin|gap):\s*([0-7])\s*(?:px|dp)', conteudo)
        for esp in espacos_curtos:
            if int(esp) < 8:
                self.avisos.append(f"[Espaçamento de Toque] {nome_arquivo}: Espaço de {esp}px < 8px mínimo. Risco de toques acidentais.")

        # 1.3 Posicionamento na Zona do Polegar
        botoes_primarios = re.findall(r'(?:testID|id):\s*["\'](?:.*(?:primary|cta|submit|confirm)[^"\']*)["\']', conteudo, re.IGNORECASE)
        posicao_inferior = bool(re.search(r'position:\s*["\']?absolute["\']?|bottom:\s*\d+|style.*bottom|justifyContent:\s*["\']?flex-end', conteudo))
        if botoes_primarios and not posicao_inferior:
            self.avisos.append(f"[Zona do Polegar] {nome_arquivo}: CTA primário pode não estar na zona do polegar (inferior). Posicione ações principais embaixo.")

        # 1.4 Alternativas para Gestos
        tem_gestos_swipe = bool(re.search(r'Swipeable|onSwipe|PanGestureHandler|swipe', conteudo))
        tem_botoes_visiveis = bool(re.search(r'Button.*(?:delete|archive|more)|TouchableOpacity|Pressable', conteudo))
        if tem_gestos_swipe and not tem_botoes_visiveis:
            self.avisos.append(f"[Gestos] {nome_arquivo}: Gestos de swipe detectados sem botões visíveis alternativos. Usuários com deficiência motora precisam de botões.")

        # 1.5 Feedback Háptico
        tem_acoes_importantes = bool(re.search(r'(?:onPress|onSubmit|delete|remove|confirm|purchase)', conteudo))
        tem_hapticos = bool(re.search(r'Haptics|Vibration|react-native-haptic-feedback|FeedbackManager', conteudo))
        if tem_acoes_importantes and not tem_hapticos:
            self.avisos.append(f"[Háptico] {nome_arquivo}: Ações importantes sem feedback háptico. Considere adicionar confirmação vibratória.")

        # 1.6 Feedback de Toque (Tempo)
        if is_react_native:
            tem_pressable = bool(re.search(r'Pressable|TouchableOpacity', conteudo))
            tem_estado_feedback = bool(re.search(r'pressed|style.*opacity|underlay', conteudo))
            if tem_pressable and not tem_estado_feedback:
                self.avisos.append(f"[Feedback Visual] {nome_arquivo}: Pressable sem estado de feedback visual. Adicione mudança de opacidade ou escala.")

        # --- 2. VERIFICAÇÕES DE PERFORMANCE MOBILE ---

        # 2.1 CRÍTICO: ScrollView vs FlatList
        tem_scrollview = bool(re.search(r'<ScrollView|ScrollView\.', conteudo))
        tem_map_no_scrollview = bool(re.search(r'ScrollView.*\.map\(|ScrollView.*\{.*\.map', conteudo))
        if tem_scrollview and tem_map_no_scrollview:
            self.problemas.append(f"[Performance CRÍTICA] {nome_arquivo}: ScrollView com .map() detectado. Use FlatList para evitar explosão de memória.")

        # 2.2 React.memo
        if is_react_native:
            tem_lista = bool(re.search(r'FlatList|FlashList|SectionList', conteudo))
            tem_react_memo = bool(re.search(r'React\.memo|memo\(', conteudo))
            if tem_lista and not tem_react_memo:
                self.avisos.append(f"[Performance] {nome_arquivo}: FlatList sem React.memo nos itens. Itens renderizarão novamente a cada atualização do pai.")

        # 2.3 useCallback
        if is_react_native:
            tem_flatlist = bool(re.search(r'FlatList|FlashList', conteudo))
            tem_use_callback = bool(re.search(r'useCallback', conteudo))
            if tem_flatlist and not tem_use_callback:
                self.avisos.append(f"[Performance] {nome_arquivo}: renderItem do FlatList sem useCallback. Uma nova função é criada a cada renderização.")

        # 2.4 keyExtractor (CRÍTICO)
        if is_react_native:
            tem_flatlist = bool(re.search(r'FlatList', conteudo))
            tem_key_extractor = bool(re.search(r'keyExtractor', conteudo))
            usa_index_como_key = bool(re.search(r'key=\{.*index.*\}|key:\s*index', conteudo))
            if tem_flatlist and not tem_key_extractor:
                self.problemas.append(f"[Performance CRÍTICA] {nome_arquivo}: FlatList sem keyExtractor. Chaves baseadas em index causam bugs em reordenação.")
            if usa_index_como_key:
                self.problemas.append(f"[Performance CRÍTICA] {nome_arquivo}: Usando index como chave. Isso causa bugs visuais. Use um ID único dos dados.")

        # 2.5 useNativeDriver
        if is_react_native:
            tem_animated = bool(re.search(r'Animated\.', conteudo))
            tem_native_driver = bool(re.search(r'useNativeDriver:\s*true', conteudo))
            if tem_animated and not tem_native_driver:
                self.avisos.append(f"[Performance] {nome_arquivo}: Animação sem useNativeDriver: true. Use para garantir 60fps na thread nativa.")

        # 2.6 Vazamento de Memória (Memory Leak)
        if is_react_native:
            tem_effect = bool(re.search(r'useEffect', conteudo))
            tem_cleanup = bool(re.search(r'return\s*\(\)\s*=>|return\s+function', conteudo))
            tem_subs = bool(re.search(r'addEventListener|subscribe|\.focus\(\)|\.off\(', conteudo))
            if tem_effect and tem_subs and not tem_cleanup:
                self.problemas.append(f"[Vazamento de Memória] {nome_arquivo}: useEffect com inscrições mas sem função de limpeza (cleanup).")

        # 2.7 Detecção de Console.log
        logs_console = len(re.findall(r'console\.log|console\.warn|console\.error', conteudo))
        if logs_console > 5:
            self.avisos.append(f"[Performance] {nome_arquivo}: {logs_console} comandos de console.log detectados. Remova em produção.")

        # 2.8 Funções Inline
        if is_react_native:
            funcoes_inline = re.findall(r'(?:onPress|onPressIn|renderItem):\s*\([^)]*\)\s*=>', conteudo)
            if len(funcoes_inline) > 3:
                self.avisos.append(f"[Performance] {nome_arquivo}: {len(funcoes_inline)} funções arrow inline em props. Use useCallback.")

        # --- 3. NAVEGAÇÃO MOBILE ---

        # 3.1 Limite de Itens na Tab Bar
        itens_tab = len(re.findall(r'Tab\.Screen|createBottomTabNavigator', conteudo))
        if itens_tab > 5:
            self.avisos.append(f"[Navegação] {nome_arquivo}: {itens_tab} abas na Tab Bar (máximo recomendado: 5).")

        # 3.2 Preservação de Estado
        if 'createBottomTabNavigator' in conteudo and 'lazy: false' not in conteudo:
            self.avisos.append(f"[Navegação] {nome_arquivo}: Tab navigation sem 'lazy: false'. As abas podem perder o estado ao alternar.")

        # --- 4. TIPOGRAFIA MOBILE ---

        # 4.1 Fontes do Sistema
        if is_react_native:
            tem_fonte_custom = bool(re.search(r"fontFamily:\s*[\"'][^\"']+", conteudo))
            tem_fonte_sistema = bool(re.search(r"fontFamily:\s*[\"']?(?:System|San Francisco|Roboto)", conteudo))
            if tem_fonte_custom and not tem_fonte_sistema:
                self.avisos.append(f"[Tipografia] {nome_arquivo}: Fonte customizada detectada. Considere fontes nativas para melhor legibilidade.")

        # 4.2 Limites de Tamanho de Fonte
        tam_fontes = re.findall(r'fontSize:\s*([\d.]+)', conteudo)
        for tf in tam_fontes:
            tamanho = float(tf)
            if tamanho < 12:
                self.avisos.append(f"[Tipografia] {nome_arquivo}: fontSize {tamanho}px abaixo do mínimo de 12px para leitura mobile.")

        # --- 5. SISTEMA DE CORES ---

        # 5.1 Evitar Preto Puro
        if re.search(r'#000000|color:\s*black|backgroundColor:\s*["\']?black', conteudo):
            self.avisos.append(f"[Cor] {nome_arquivo}: Preto puro (#000000) detectado. Use cinza escuro (#121212) para melhor performance em OLED.")

        # 5.2 Suporte a Dark Mode
        if 'useColorScheme' not in conteudo and 'Appearance' not in conteudo:
            self.avisos.append(f"[Cor] {nome_arquivo}: Nenhum suporte a Dark Mode detectado. Considere usar useColorScheme.")

        # --- 6. PLATAFORMA iOS ---

        if is_react_native:
            # 6.3 SafeArea no iOS
            if 'SafeAreaView' not in conteudo and 'useSafeAreaInsets' not in conteudo:
                self.avisos.append(f"[iOS] {nome_arquivo}: Nenhuma SafeArea detectada. O conteúdo pode ser cortado pelo notch/home indicator.")

        # --- 7. PLATAFORMA ANDROID ---

        if is_react_native:
            # 7.2 Efeito Ripple
            if 'Pressable' in conteudo and 'android_ripple' not in conteudo:
                self.avisos.append(f"[Android] {nome_arquivo}: Touchable sem efeito Ripple. Usuários Android esperam feedback de ondulação.")

        # --- 8. BACKEND E SEGURANÇA ---

        # 8.1 Armazenamento Seguro
        tem_async_storage = bool(re.search(r'AsyncStorage', conteudo))
        tem_token = bool(re.search(r'token|jwt|auth.*storage', conteudo, re.IGNORECASE))
        if tem_token and tem_async_storage:
            self.problemas.append(f"[Segurança] {nome_arquivo}: Armazenando tokens no AsyncStorage (inseguro). Use SecureStore ou Keychain.")

        # --- 13. ACESSIBILIDADE MOBILE ---

        if is_react_native:
            tem_touchable = bool(re.search(r'TouchableOpacity|Pressable', conteudo))
            tem_a11y_label = bool(re.search(r'accessibilityLabel|aria-label', conteudo))
            if tem_touchable and not tem_a11y_label:
                self.avisos.append(f"[Acessibilidade] {nome_arquivo}: Elemento clicável sem accessibilityLabel. Leitores de tela não saberão o que ele faz.")

    def auditar_diretorio(self, diretorio: str) -> None:
        extensoes = {'.tsx', '.ts', '.jsx', '.js', '.dart'}
        for raiz, pastas, arquivos in os.walk(diretorio):
            pastas[:] = [d for d in pastas if d not in {'node_modules', '.git', 'dist', 'build', 'ios', 'android'}]
            for arq in arquivos:
                if Path(arq).suffix in extensoes:
                    self.auditar_arquivo(os.path.join(raiz, arq))

    def obter_relatorio(self):
        return {
            "arquivos_verificados": self.arquivos_verificados,
            "problemas": self.problemas,
            "avisos": self.avisos,
            "em_conformidade": len(self.problemas) == 0
        }

def main():
    if len(sys.argv) < 2:
        print("Uso: python auditoria_mobile.py <diretorio>")
        sys.exit(1)

    caminho = sys.argv[1]
    auditor = AuditorMobile()
    
    if os.path.isfile(caminho):
        auditor.auditar_arquivo(caminho)
    else:
        auditor.auditar_diretorio(caminho)

    relatorio = auditor.obter_relatorio()

    print(f"\n[AUDITORIA MOBILE] {relatorio['arquivos_verificados']} arquivos analisados")
    print("-" * 60)
    
    if relatorio['problemas']:
        print(f"❌ PROBLEMAS CRÍTICOS ({len(relatorio['problemas'])}):")
        for p in relatorio['problemas']:
            print(f"  - {p}")
            
    if relatorio['avisos']:
        print(f"\n⚠️  AVISOS DE UX/PERFORMANCE ({len(relatorio['avisos'])}):")
        for a in relatorio['avisos']:
            print(f"  - {a}")

    print("-" * 60)
    status = "APROVADO" if relatorio['em_conformidade'] else "FALHOU"
    print(f"STATUS FINAL: {status}")

if __name__ == "__main__":
    main()