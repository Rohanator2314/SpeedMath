# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\sroha\\Documents\\git\\T2Python\\MainProject'],
             binaries=[],
             datas=[('algebra.py', '.'), ('db.py', '.'), ('geometry.py', '.'), ('numguess.py', '.'), ('setup.py', '.'), ('speedmath.py', '.'), ('C:/Users/sroha/AppData/Local/Programs/Python/Python39/Lib/site-packages/pyfiglet', 'pyfiglet/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Speed Maths',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='speedmath.ico')
