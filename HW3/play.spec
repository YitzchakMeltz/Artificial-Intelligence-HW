# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:\\Users\\hmeltz\\Documents\\GitHub\\Artificial-Intelligence-HW\\HW3\\play.py'],
             pathex=['C:\\Users\\hmeltz\\Documents\\GitHub\\Artificial-Intelligence-HW\\HW3'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=True)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('v', None, 'OPTION')],
          name='play',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\hmeltz\\Documents\\GitHub\\Artificial-Intelligence-HW\\HW3\\Connect4Logo_1.0.0.ico')
